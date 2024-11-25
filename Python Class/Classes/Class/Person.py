
class Person:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def profileGreeting(self):
        return f"Hello my name is {self.name}"
    
    def profileBirthdayAge(self):
        self.age += 1
        return f"Happy Birthday you are {self.age} years old."
    
    def checkIfAdultProfile(self):
        if self.age < 18:
            return f"This is a restricted part of this website wait till you are older. Your age is {self.age}"
        return f"Welcome you old timer!"

    def profilePhysicalFeatures(self):
        return f"My Hair color is: {self.hair_color}, and my Eye color is {self.eye_color}"
    
    def updateProfileName(self, new_name):
        self.name = new_name
        return f"Name has been updated to: {self.name}"

    def updateAge(self, new_age):
        self.age = new_age
        return f"Age has been updated to: {new_age}"
    

