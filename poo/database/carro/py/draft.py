class Carro:
    def __init__(self, pas: int, gas: int, km: int):
        self.pas = 0
        self.gas = 0
        self.km = 0

    def passMax(self, increment: int) -> None:
        if self.pas < 2:
            self.pas += increment
        if self.pas > 2:
            self.pas = 2
            print("fail: limite de pessoas atingido")
        if self.pas < 0:
            self.pas = 0

    def gasMax(self, increment: int) -> None:
        if self.gas < 100:
            self.gas += increment
        if self.gas > 100:
            self.pas = 100
            #print("")


def __str__(self) -> str:
    print(f"pass: {self.pas}, gas: {self.gas}, km: {self.km}")

def main():
    carro = Carro("", "", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(carro)
        if args[0] == "enter":
            increment: int = int(args[1])
            carro.passMax(increment)
            if carro.pas == 2:
                print(f"fail: limite de pessoas atingido")
        if args[0] == "leave":
            carro.passMax(increment)
            if carro.pas == 0:
                print(f"fail: nao ha ninguem no carro")
        if args[0] == "fuel increment":
            carro.gasMax(increment)
            if carro.pas == 100:
                print("tanque cheio")
        if args[0] == "drive distance":
            if carro.pas == 0:
                print(f"fail: nao ha ninguem no carro")
            if carro.gas == 0:
                print(f"fail: tanque vazio")
        else:
            print("fail: comando invalido")
main()

