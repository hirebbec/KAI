import datetime

class Event:
    description = 'default description'
    date = datetime.datetime.strptime('01-01-2001', '%d-%m-%Y')

    def from_string(self, *args):
        if len(args) != 1 or isinstance(args[0], str) != True:
            raise SyntaxError('Expected string is: \'desscription * dd-mm-yyyy\'')
        list = args[0].split('*')
        if len(list) != 2:
            raise SyntaxError('Expected string is: \'desscription * dd-mm-yyyy\'')
        self.description = list[0].strip()
        self.date = datetime.datetime.strptime(list[1].strip(), '%d-%m-%Y')


event = Event()
event.from_string('Party * 11-11-1111')
print(event.date)
print(event.description)