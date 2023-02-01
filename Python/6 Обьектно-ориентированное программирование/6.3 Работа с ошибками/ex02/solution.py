class FileReader:
    def __init__(self, filename=None) -> None:
        self._filename = filename

    def read(self):
        try:
            file = open(self._filename)
            return file.read()
        except FileNotFoundError:
            return str()