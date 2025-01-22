from Person import Person as PN

class Profile:
    def __init__(self):
        self.person = PN("", 0, "", "")

    def createPerson(self):
        person = PN("Dom", 32, "Brown", "Blue")
        return person
    
    def printPersonData(self):
        print(self.createPerson().age)

new_profile = Profile()

dom = new_profile.createPerson()
print(dom.age)
print(dom.profileBirthdayAge())