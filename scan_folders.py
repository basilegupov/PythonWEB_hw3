import sys
from pathlib import Path
import param

result = {'FOLDERS': [], 'EXT': set(), 'EXT_UNKNOWN': set()}


def init_result():
    global result
    
    for item in param.WORK_FOLDERS:
        result[item.upper()] = []
    return 'Ok'


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan_folder_rec(folder):

    for item in folder.iterdir():
        
        if item.is_dir():
           
            if item.name.upper() not in param.WORK_FOLDERS:
                result['FOLDERS'].append(item)
                scan_folder_rec(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            result['OTHER'].append(new_name)
        else:
            try:
                result[param.WORK_EXTENTIONS[extension]].append(new_name)
                result['EXT'].add(extension)
            except KeyError:
                result['OTHER'].append(new_name)
                result['EXT_UNKNOWN'].add(extension)


def scan_folder(folder):
    init_result()
    scan_folder_rec(folder)


def out_log_folder_rec(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name in param.WORK_FOLDERS and item.name.upper() != 'ARCHIVES':
                result['FOLDERS'].append(item)
                out_log_folder_rec(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = item.name

        if not extension:
            result['OTHER'].append(new_name)
        else:
            try:
                result[param.WORK_EXTENTIONS[extension]].append(new_name)
                result['EXT'].add(extension)
            except KeyError:
                result['OTHER'].append(new_name)
                result['EXT_UNKNOWN'].add(extension)


def out_log_folder(folder, file_log='scan.log'):
    init_result()
    out_log_folder_rec(folder)

    items = [item for item in result]

    with open(file_log, 'w') as f_out:
        for item in items:
            if item != 'ARCHIVES' and item != 'FOLDERS':
                f_out.write(f'{item}:\n')
                for file in result[item]:
                    f_out.write(f'  {file}\n')


if __name__ == '__main__':

    path = sys.argv[1]
    print(f"Start in {path}")
    folder = Path(path)

    scan_folder(folder)
    for key, res in result.items():
        print(f'{key}:{res}')

    out_log_folder(folder)
