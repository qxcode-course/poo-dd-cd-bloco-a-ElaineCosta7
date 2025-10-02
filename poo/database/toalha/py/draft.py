class Towel: #em algumas linguagens chamada de this
    def __init__(self, color: str, size: str): #construtor (ele cria os objetos da classe)
        self.color: str = color #atributos
        self.size: str = size
        self.wetness: int = 0
        # 'def' cria a função/método
        # self é o objeto que manipulamos

# def são metodos/funções que dão certos comportamentos a class
    def dry(self, amount: int) -> None: # seca a toalha
        self.wetness += amount # aumenta a umidade da toalha
        if self.wetness >= self.getMaxWetness(): # indica que a quantidade de água ultrapassa o máximo que pode ser retido
            print('toalha encharcada')
            self.wetness = self.getMaxWetness() # limita o maximo de água que a toalha pode reter


    def isDry(self) -> bool: # verifica se a toalha está seca
        return self.wetness == 0

    def wringOut(self) -> None:  # torce/enxuga a toalha
        self.wetness = 0 # não utiliza return pois atribui um valor à variavel, e não apenas retorna seu valor 
    # wringOut tira a umidade/iguala a zero, isDry verifica se a umidade é zero


    def getMaxWetness(self) -> int: # identifica o quanto de liquido a toalha retem de acordo com tamanho
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 # caso o tamanho não seja nenhum anterior, como 'GG' ou 'XG'
        # não é preciso usar else, pois o return encerra esta função


    def __str__(self) -> str: #toString (converte um objeto em texto)
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"


def main(): # 2. tranforma o código em algo interativo ao usuário
    toalha = Towel("", "") # 3. cria um objeto vazio/template, manipulável
    while True: # 4. mantem o usuário preso em um loop de interação, onde é dito como deseja manipular a 'toalha'
        line: str = input() # 5. o que o usuário deseja fazer? quais dos comandos vai utilizar
        args: list[str] = line.split(" ") # 6. lista palavras chaves das funções que deseja rodar, line.split separa palavras de acordo com espaço
        if args[0] == "end": # se usuario quer ir embora, ele recebe end
            break # sai do loop 
        elif args[0] == "new": # cria uma nova
            color = args[1] # cor pertence ao parametro 1
            size = args[2] # pertencente a posição 2
            toalha = Towel(color, size) # preenche as duas informações de um vez
        elif args[0] == "show": # mostra o estado atual do objeto criado
            print(toalha) 
        elif args[0] == "dry": # chama a função dry
            amount: int = int(args[1]) # transforma o inteiro para entrar na lista de strings
            toalha.dry(amount) # indica quanto secar
        else:
            print("fail: comando inválido") # 7. caso o comando seja qualquer outro não existente
            



main() # 1. chama a função main, sempre tem que estar no final do código

# transformou um código linear em um iterativo