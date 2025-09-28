class Animal:
    def __init__ (self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def ageBy(self, increment: int) -> None:
        if self.age < 4:
            self.age += increment
            if self.age > 4:
                self.age + 4
        
        if self.age == 0:
            return "filhote"
        elif self.age == 1:
            return "criança"
        elif self.age == 2:
            return "adulto"
        elif self.age == 3:
            return "idoso"
        elif self.age == 4:
            return "morto"
        elif self.age >= 4:
            print(f"warning: {self.species} morreu")

    def makeSound(self) -> str:
        if self.age == 0:
            print("---")
        if self.age == 4:
            print("RIP")
        if self.age == 1 or self.age == 2 or self.age == 3:
            print(self.sound)

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"


def main():
    animal = Animal("", "")
    while True:
        line: str = input()
        print("$" + line) # eco
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            print(animal)
        elif args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
            if animal.age == 4:
                print(f"warning: {animal.species} morreu")
        elif args[0] == "noise":
            animal.makeSound()
        else:
            print("fail: comando inválido")

main()