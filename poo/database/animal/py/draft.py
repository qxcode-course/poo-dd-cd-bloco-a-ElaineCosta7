class Animal:
    def __init__ (self, species: str, age: int, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"


def main():
    animal = Animal("", "")
    while True
        line: 