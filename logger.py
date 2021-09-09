import hashlib
from main import path_logg, get_path

@get_path(path_logg)

def get_md5(path):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

for elm in get_md5('wiki'):
    print(elm)