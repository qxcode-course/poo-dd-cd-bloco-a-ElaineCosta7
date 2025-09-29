class Carro:
    def __init__(self, pas: int, gas: int, km: int):
        self.pas = 0
        self.gas = 0
        self.km = 0

    def passMax(self, increment: int) -> None:
        self.pas += increment
        if self.pas > 2:
            self.pas = 2
            print(f"fail: limite de pessoas atingido")
        if self.pas < 0:
            self.pas = 0
            print(f"fail: nao ha ninguem no carro")

    def gasMax(self, increment: int) -> None:
        if self.gas < 100:
            self.gas += increment
        if self.gas > 100:
            self.gas = 100
            #print("")


    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"

def main():
    carro = Carro("", "", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.passMax(1)
        elif args[0] == "leave":
            carro.passMax(-1)
        elif args[0] == "fuel":
            increment: int = int(args[1])
            carro.gasMax(increment)
        elif args[0] == "drive":
            dist = int(args[1])
            if carro.pas == 0:
                print(f"fail: nao ha ninguem no carro")
            elif carro.gas == 0:
                print(f"fail: tanque vazio")
            else:
                if carro.gas < dist:
                    carro.km += carro.gas
                    percorrido = carro.gas
                    carro.gas = 0
                    print(f"fail: tanque vazio apos andar {percorrido}" + " km")
                else:
                    carro.km += dist
                    carro.gas -= dist
        else:
            print("fail: comando invalido")
main()

