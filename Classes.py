
class Human:
    """This is a test to display the doctype"""
    def __init__(self):
        print('I am a human being')

    def speak(self):
        print('Hello')

    def walk(self):
        print('I walk up-right')

'''class Person(Human):
    def __init__(self):
        Human.__init__(self)

    #print(Human.speak())
    print(Human.walk())'''

#h = Person()
help(Human)

'''
class TestClass:
    def __init__(self, name, surname, yearOfBirth):
        self.name = name
        self.surname = surname
        self.yearOfBirth = yearOfBirth

    def setName(self, nm):
        self.name = nm

    def setSurname(self, sname):
        self.surname = sname

    def setYearOfBirth(self, yob):
        self.yearOfBirth = yob

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    @property
    def getYearOfBirth(self):
        return self.yearOfBirth

    def toString(self):
        print('My name is {} {} I was born in {}, I\'m now {} year old'.format(self.name, self.surname, self.yearOfBirth,
                                                                              (2017 - self.yearOfBirth)))

t = TestClass('Banele', 'Mlamleli', 1992)
t1 = TestClass('Siphosethu', 'Mhlanga', 1993)
#t.toString()
#t1.toString()
print(hasattr(t, 'name'))
print(dir(t))

'''