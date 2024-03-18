def get_params():
    result = {}
    with open('param.ini', 'r') as file:
        for line in file:

            if len(line.strip()) > 0:
                if line.strip()[0] == '#' or line.strip()[0] == ';':
                    continue
                folder, exten = line.strip().split(':')
                exten = exten.strip().split(',')

                for ext in exten:
                    result[ext.strip().upper()] = str(folder).strip().upper()
    return result


WORK_EXTENTIONS = get_params()

if len(WORK_EXTENTIONS) == 0:
    WORK_EXTENTIONS = {
        'JPEG': 'IMAGES', 'PNG': 'IMAGES', 'JPG': 'IMAGES', 'SVG': 'IMAGES',
        'AVI': 'VIDEO', 'MP4': 'VIDEO', 'MOV': 'VIDEO', 'MKV': 'VIDEO',
        'DOC': 'DOCUMENTS', 'DOCX': 'DOCUMENTS', 'TXT': 'DOCUMENTS',
        'PDF': 'DOCUMENTS', 'XLSX': 'DOCUMENTS', 'PPTX': 'DOCUMENTS',
        'MP3': 'AUDIO', 'OGG': 'AUDIO', 'WAV': 'AUDIO', 'AMR': 'AUDIO',
        'ZIP': 'ARCHIVES', 'GZ': 'ARCHIVES', 'TAR': 'ARCHIVES',
        '*': 'OTHER'}

WORK_FOLDERS = set([fold.lower() for ext, fold in WORK_EXTENTIONS.items()])

if __name__ == '__main__':
    print(WORK_EXTENTIONS)
    print(WORK_FOLDERS)
    print(get_params())
# зображення ('JPEG', 'PNG', 'JPG', 'SVG');
# відеофайли ('AVI', 'MP4', 'MOV', 'MKV');
# документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
# музика ('MP3', 'OGG', 'WAV', 'AMR');
# архіви ('ZIP', 'GZ', 'TAR');
# невідомі розширення.

# зображення переносимо до папки images
# документи переносимо до папки documents
# аудіо файли переносимо до audio
# відео файли до video
# архіви розпаковуються, та їх вміст переноситься до папки archives
# файли з невідомими розширеннями скласти в папку other


# d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

# keys = [k for k, v in d.items() if v == 'aaa']
# print(keys)
# # ['key1', 'key2']

# keys = list()
# for k, v in d.items():
#     if v == 'aaa':
#         keys.append(k)

# print(keys)
