estoque = {} 

def adicionarLivro():
    titulo = input("\ntitulo do livro:").strip
    qtd = int(input("\nQuantidade a adicionar: "))

    if titulo in estoque:
        estoque[titulo] += qtd
    else:
        estoque[titulo] = qtd
    print(f"\n{qtd} unidade(s) de '{titulo}' adicionada(s)\n")
    
def removerLivro():
    pass

def consultarLivro():
    pass

def mostrarEstoque():
    if not estoque:
        print("\nEstoque vazio.\n")
        return

    print(f"\nLivros em estoque\n")
    # pega a chave do dicionario e imprime pela chave
    for titulo in sorted(estoque.keys()):
        print(f"\n{titulo}: {estoque[titulo]}\n")
    
def main():
    while True:
        print("\n--- MENU ---\n")
        print("1. Adicionar um livro ao estoque")
        print("2. Remover unidades de um livro")
        print("3. Consultar quantidade de um livro")
        print("4. Mostrar todos os livros com suas quantidades ordenados alfabeticamente")
        print("5. Sair ")
        
        opcao = input("\nEscolha uma opção [1-6]\n").strip()
        if opcao == "1":
            adicionarLivro()
        elif opcao == "2":
            removerLivro()
        elif opcao == "3":
            consultarLivro()
        elif opcao == "4":
            mostrarEstoque()
        elif opcao == "6":
            print("\nEncerrando o programam! Ate mais.")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()