Compras = []

while True:
    print("Selecione uma opção abaixo: \n" \
          "1- Adicione um item a lista\n" \
            "2- Remover um item da lista\n" \
            "3- Limpar a lista\n" \
            "4- Mostrar a lista\n" \
            "5- Sair")
    Opcao = int(input("Digite a opção desejada"))

    if Opcao == 1:
        produto = str(input("Digite o item que você quer adicionar a lista:"))
        Compras.append(produto)
        print("item adicionado da lista")
    elif Opcao == 2:
        produto = str(input("Digite o item que você quer remover da lista"))
        Compras.remover(produto)
        print("item removido da lista")
    elif Opcao == 3:
        Compras.clear()
        print("lista limpa")
    elif Opcao == 4:
        print("compras")
    elif Opcao == 5:
        print("obrigado por utilizar nosso programa")
        break
    else:
        print("Digite uma opção válida")
