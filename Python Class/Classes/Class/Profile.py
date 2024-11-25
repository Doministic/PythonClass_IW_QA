import Classes.Class.Person as Person

class Profile:
    def __init__(self):
        self.person = Person("", 0, "", "")

    def createPerson(self):
        person = Person("Dom", 32, "Brown", "Blue")
        return person
    
    def printPersonData(self):
        print(self.createPerson())

Profile().printPersonData()
