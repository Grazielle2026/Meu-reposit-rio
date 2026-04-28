def menu():
    print("-=-CONVERSOR DE TEMPERATURA-=- \n" \
    "1 - Celsius para Fahrenheit \n" \
    "2 - Fahrenheit para Celsius \n" \
    "3 - Celsius para Kelvin \n" \
    "4 - Fahrenheit para Kelvin \n" \
    "5 - Kelvin para Celsius \n" \
    "6 - Kelvin para Fahrenheit")
    opcao = int(input("Escolha uma opção:"))
    temp = float(input("Digite a temoperatura para conversão:"))

    match opcao:
        case 1:
            return 0 
        case 2:
            return 0
        case 3:
            return 0
        case 4:
            return 0
        case 5:
            return 0
        case 6:
            return 0
        case _:
            print("opçãon ínvalida")

def CpF(X):
    res = (X * (9/5)) + 32
    print(f'{X}°F equivalem a {res: .2f}°C')

def FpC(X):
    res = (X - 32) * (5/9)
    print(f' {X}°F equivalem a {res: .2f}°C')

def CpK(X):
    res = X + 273.15
    print(f'{X}/C equivalem a {res: 2.f}°K')

def KpF(X):
    res =(X - 32) * (5/9) + 273.15
    print(f'{X}°F rquivalem a {res: .2f}°K')
    
def KpC(X):
    res = X - 273.15
    print(f'{X}°K equivalem a {res: .2f}°C')

def KpF(X):
    res = (X - 273.15) * (9/5) + 32
    print(f'{X}°K equivalem a {res: .2f}°F')

menu()