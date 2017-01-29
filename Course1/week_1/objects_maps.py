class Person(object):
    department = 'School of Information'

    def SetName(self, new_name):
        self.name = new_name

    def SetLocation(self, new_location):
        self.location = new_location

person = Person()
person.SetName('Chrsitopher Books')
person.SetLocation('Ann Arbor')

print('{} live in {} works in the department {}'.format(person.name, person.location, person.department))