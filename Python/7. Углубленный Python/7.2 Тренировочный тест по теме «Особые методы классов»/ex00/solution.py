import tempfile
import os
import uuid

class File:
    def __init__(self, path):
        self._path = path
        if os.path.exists(self._path) == False:
            with open(self._path, 'w') as file:
                pass            

    def __str__(self):
        return self._path

    def read(self):
        with open(self._path, 'r') as file:
            return file.read()

    def write(self, text):
        with open(self._path, 'w') as file:
            return file.write(text)

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        new_file_obj = File(new_path)
        new_file_obj.write(str(self.read()) + str(other.read()))
        return new_file_obj

    def __iter__(self):
        with open(self._path, 'r') as file:
            for line in file.readlines():
                yield line

    def __next___(self):
        generator = self.__iter__()
        return next(generator)
