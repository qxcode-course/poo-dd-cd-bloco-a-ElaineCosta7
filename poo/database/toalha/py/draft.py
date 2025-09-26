class Towel:
    def __init__(self, color): #construtor
        self.color = 'yellow' #atributos
        self.size = 'm'
        self.wetness = 0

#referencia
towel = Towel() #objetos

print(towel.color)
print(towel.size)
print(towel.wetness)