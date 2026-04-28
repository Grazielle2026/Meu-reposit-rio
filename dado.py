from random import randint

def main():
    while True:
        resultados = []
        print("--Simulador de Dados--")
       
        # Escolher o número de lados do dado
        lados = int(input("Quantos lados o dado deve ter? (4, 6, 8, 10, 12, 20, 100): "))
        if lados not in [4, 6, 8, 10, 12, 20, 100]:
            print("Número de lados inválido! Escolha entre 4, 6, 8, 10, 12, 20, ou 100.")
            continue
       
        # Perguntar a quantidade de dados a serem rolados
        quantidade = int(input("Quantos dados você quer rolar? "))
        if quantidade <= 0:
            print("Quantidade inválida!")
            continue
        else:
            for i in range(quantidade):
                rolagem = randint(1, lados)  # Rola um dado com 'lados' faces
                resultados.append(rolagem)

        # Exibir os resultados
        print(f'A soma das rolagens foram: {sum(resultados)}')
        print(f'As rolagens foram: {resultados}')

main()