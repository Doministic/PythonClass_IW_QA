
class Animal:
    def __init__(self, name, age):
        self.species = ""
        self._name = name
        self._age = age

class Feline(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def get_species(self):
        pass      

class Cat(Feline):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_species(self):
        return "This is a Domesticated House Cat"


cat = Feline("Phantom", 18)
dsh_cat = Cat("Tucker", 18)


print(cat.get_species())
print(dsh_cat.get_species())