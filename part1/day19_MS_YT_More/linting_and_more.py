presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Keke', 'age': 41}
]

print(presenters)
presenters.sort(key=lambda item: item['name'])
print(presenters)

import pathlib
print(pathlib.Path.cwd())