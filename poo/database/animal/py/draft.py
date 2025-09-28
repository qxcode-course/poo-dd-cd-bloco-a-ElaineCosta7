class Animal:
    def __init__ (self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def ageBy(self, increment: int) -> none:
        self.age += increment


    def lifeStage(self) -> none:
        if self.age == 0:
            return "filhote"
        if self.age == 1:
            return "criança"
        if self.age == 2:
            return "adulta"
        if self.age == 3:
            return "idoso"
        if self.age == 4:
            return "morto"
        if self.age > 4:
            print(f"warning: {self.species} morreu")


    def makeSound(self) -> str:
        self.age == 0
            return "---"
        self.age == 4:
            return "RIP"
        self.age == 1 or self.age == 2 or self.age ==3:
            return self.sound

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"


def main():
    animal = Animal("", "")
    while True:
        line: str = input()
        print(f"${line}") # eco
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "ageBy":
            increment: int = int(args[1])
            animal.ageBy(increment)
        else:
            print("fail: comando inválido")


main() 

