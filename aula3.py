from math import log10

def menu():
    while True:
        print("Calculadora de escalas logaritmicas")
        print("Selecione uma opção abaixo: \n"\
        "1 - Escala ph \n" \
        "2 - Escala Richter \n" \
        "3 - Sair")    
        opcao = int(input("Escolha: "))

        if opcao == 1:
            ph()
        elif opcao == 2:
            richter() 
        elif opcao == 3:
            print("Até logo!")
            break
        else:
            print("Opção inválida")

def ph():
    print("Escala de PH")
    print("------------")

    while True:
        print("Para sair do programa, digite 0")
        h30 = float(input("Digite a quantidade de H30/mol na substância: "))

        if h30 == 0:
            print("Saindo")
            break

    else:
        ph = -1 * log10(h30)
    if ph > 0 and ph < 7:
        print(f'O pH de {ph:.2f} é considerado ácido')
    elif ph < 7 and ph <= 14:
        print(f'O pH de {ph:.2f} é considerado alcalino')
    else:
        print("O pH não pode ser calculado")

def richter():
    print("Escala Richter")
    print("---------------")

    while True:
        print("selecione uma opção abaixo: \n" \
        "1 - Joules para Magnetude \n" \
        "2 - Magnetude para Jaules \n" \
        "3 - Voltar o Menu Principal")
        opcao = int(input("Opção Escolhida: "))

    if opcao == 1:
        joules = float(input("Digite a quantidade de energia(Joules)"))
        if joules <= 0:
            print("Quantidade de energia inválida")
        else:
            res = (log10(joules - 4.8)) / 1.5
            print(f'A Magnetude do terremoto é de {res:.2f} na escala Richter')
    elif opcao == 2:
        magnetude = float(input("Digite a magnetude do terremoto"))
        if magnetude <= 0:
            print("Magnetude inválida!")
        else:
            res = 10 ** (1.5 * magnetude + 4.8)
            print(f'A magnetude equivale a {res:.2f} Joules de Energia')
    elif opcao == 3:
        breakpoint
        
menu()
    