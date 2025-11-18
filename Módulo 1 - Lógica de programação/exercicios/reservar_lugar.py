lugares = [False] * 10

def reservarAssento():
    n = int(input("Qual número do lugar que deseja reservar [1-10]"))
    
    if 1 <= n <= 10:
        if lugares[n - 1] == False:
            lugares[n - 1] == True
            print(f"Assento {n} reservado com sucesso.")
        else:
            print(f"\nAssento {n} já está oculpado.\n")
    else:
        print("\nNúmero de assento inválido\n")

def liberarAssento():
    pass
def mostrarMapa():
    print("\nMapa de Ocupação dos Assentos:\n")
    for i in range(10):
        if lugares[i] == True:
            status = "Oculpado"
        else:
            status = "Livre"
        print(f"Assento {n} ")

def main():
    while True:
        print("\n---Menu Cinema---\n")
        print("1. Reservar um assento")
        print("2. Liberar um assento")
        print("3. Mostrar mapa de ocupação")
        print("4. Sair")
        opcao = input("\nEscolha uma opção [1-4]\n")
        if opcao == "1":
            reservarAssento()
        elif opcao == "2":
            liberarAssento()
        elif opcao == "3":
            mostrarMapa()
        elif opcao == "4":
            print("\nEncerrando o programam! Ate mais.")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()