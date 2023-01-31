#Импорты
import argparse
import json
import tempfile
import os
 
# #Реализуем парсер
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(storage_path):#Файл существует
    if args.value == None:
        try:
            with open(storage_path, 'r') as file:
                dict = json.load(file)
                if type(dict[args.key]) is list:
                    print(', '.join(dict[args.key]))
                else:
                    print(dict[args.key])
        except:
            print(None)
    else:
        with open(storage_path, 'r') as file:
            dict = json.load(file)
            if args.key in dict:
                try:
                    dict[args.key].append(args.value)
                except AttributeError:
                    dict[args.key] = [dict[args.key], args.value]
            else:
                dict[args.key] = args.value
        with open(storage_path, 'w') as file:
            json.dump(dict, file)
else:#Если файл не существует
    if (args.value == None):
        print(None)
    else:
        with open(storage_path, 'w') as file:
            json.dump({}, file)
        with open(storage_path, 'r') as file:
            dict = json.load(file)
            dict[args.key] = args.value
        with open(storage_path, 'w') as file:
            json.dump(dict, file)
