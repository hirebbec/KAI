try:
    file = open('names.txt', 'r')
except FileExistsError or FileNotFoundError as e:
    print(e.errno)
except:
    print('Unexpected error')

class MyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        return f"Name is to short --> {self.message}"
count = 0
for str in file:
    if len(str) < 5:
        raise MyException(str)
    count += len(str)
print(count)