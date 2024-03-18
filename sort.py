import sys
from pathlib import Path
import threading
import shutil
import normalize
import scan_folders


def handle_file(path: Path, root_folder: Path, dist: Path):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))
    

def handle_archive(path: Path, root_folder: Path, dist: Path):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    new_name = normalize.normalize(path.name.split('.')[0])
    archive_folder = target_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        path.unlink()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        path.unlink()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass


def main(folder_path):
    
    scan_folders.scan_folder(folder_path)

    threads = []
    for item in scan_folders.result:

        if item not in ('FOLDERS', 'EXT', 'EXT_UNKNOWN', 'ARCHIVES'):
            for file in scan_folders.result[item]:
                thread = threading.Thread(target=handle_file,
                                          args=(file, folder_path, item.lower()))
                threads.append(thread)
                thread.start()

    for file in scan_folders.result['ARCHIVES']:
        thread = threading.Thread(target=handle_archive,
                                  args=(file, folder_path, 'ARCHIVES'.lower()))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    remove_empty_folders(folder_path)

    scan_folders.out_log_folder(folder_path)
    

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Укажите целевую папку.')
        exit()
    else:
        path = sys.argv[1]

    print(f'Start in {path}')

    folder = Path(path)
    
    main(folder.resolve())
