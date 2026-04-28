def menu()
    print("Selecione a progressão desejada: \n" \
    "1- Progressão Aritimética(PA): \n" \
    "2- Progressão Geométrica(PG)")
opcao = int(input("Escolha uma opção: "))
num = int(input("Selecione o 1° número da prgressão"))
r = int(input("Escolha a razão da progressão"))
match opcao:
    case 1:
        PA(num, r)
    case 2:
        PG(num, r)
    case 3:
        print = ("opção invaçida!")

def PA(num,)