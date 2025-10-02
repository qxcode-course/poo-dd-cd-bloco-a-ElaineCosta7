class Calculadora:
    def __init__(self, batteryMax: int, battery: int): #valha
        self.display: int = 0
        self.battery: int = 0 
        self.batteryMax: int = batteryMax
        

    def charge(self, increment: int) -> int:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: int, b: int) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.battery -= 1
            self.display = a + b


    def div(self, num: int, den: int) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif num == 0 or den == 0:
            print("fail: divisao por zero")
            self.battery -= 1
        else:
            self.battery -= 1
            self.display = num / den 


    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
def main():
        calculadora = Calculadora("", "")
        while True:
            line: str = input()
            print("$" + line)
            args: list[str] = line.split(" ")
            if args[0] == "end":
                break
            elif args[0] == "init":
                display = int(args[1])
                batteryMax = args[0]
                calculadora = Calculadora(display, batteryMax)
            elif args[0] == "show":
                print(calculadora)
            elif args[0] == "charge":
                increment: int = int(args[1])
                calculadora.charge(increment)
            elif args[0] == "sum":
                a = int(args[1])
                b = int(args[2])
                calculadora.sum(a, b)
            elif args[0] == "div":
                num = int(args[1])
                den = int(args[2])
                calculadora.div(num, den)
            else:
                print("fail: comando invalido") 

main()