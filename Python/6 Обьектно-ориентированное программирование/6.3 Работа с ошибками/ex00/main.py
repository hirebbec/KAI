filename = input("Имя нового файла: ")
text = input("Текс файла: ")

try:
    file = open(filename)
    file.write(text)
except FileExistsError as e:
    print(e.errno)
except FileNotFoundError as e:
    print(e.errno)
except:
    print('Unexpected error')
finally:
    file.close()