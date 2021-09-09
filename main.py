from datetime import datetime
import json
import random

def get_path(path):
    path = f'{path}\logg_file.json'
    def decorator(old):
        def logger(*args, **kwargs):
            logg = f'{datetime.now()} вызвана функция {old.__name__} с аргументами {args}{kwargs}'
            result = old(*args, **kwargs)
            with open('logg_file.json', 'w', encoding='UTF-8') as file:
                json.dump(logg, file, ensure_ascii=False, indent=2)

            return result
        return logger
    return decorator

path_logg = input('введите путь к логам: ')
@get_path(path_logg)
def foo(a, b):
    print(random.randint(a, b))

foo(19, 25)


