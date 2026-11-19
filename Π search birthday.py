from pathlib import Path

path = Path(r"F:\py learining flie\test\Π")
my_birthday = '916'

search = ''
contents = path.read_text()

for i in contents.splitlines():
    search += i.strip()

if my_birthday in search:
    print('your birthday is in Π')
else:
    print('sorry')