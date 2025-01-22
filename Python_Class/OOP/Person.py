
class Animal:
    def __init__(self, name, age):
        self.species = ""
        self._name = name
        self._age = age

    def _Speak(self):
        pass

class Feline(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def _Speak(self):
        return "Meow"

    def get_species(self):
        return "Feline"     

class House_Cat(Feline):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_species(self):
        return "This is a Domesticated House Cat"

class Canine(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def _Speak(self):
        return "woof"

    def get_species(self):
        return "Canine"

canine = Canine("Artemis", 6)
dsh_cat = House_Cat("Tucker", 18)


print(canine._Speak())
print(dsh_cat._Speak())
