import re

UKR_SYM = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i",
               "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for key, val in zip(UKR_SYM, TRANSLATION):
    TRANS[ord(key)] = val
    TRANS[ord(key.upper())] = val.upper()


def normalize(name: str) -> str:
    name, *ext = name.split('.')
    name = name.translate(TRANS)
    name = re.sub(r'\W', '_', name)
    if len(ext) == 0:
        return name
    return f"{name}.{'.'.join(ext)}"


if __name__ == '__main__':
    print(normalize('Іс~ХО)іX.tar.gz'))
    print(normalize('Іс~ХО)іX'))
