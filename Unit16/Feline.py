
class Pet:
    def __init__(self, species, name, gender, age):
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age

#сажаем каждую позицию на функцию. при обращении к ней аналогичнй определенному в классе вызов
    def getSpecies(self):
        return self.species

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age