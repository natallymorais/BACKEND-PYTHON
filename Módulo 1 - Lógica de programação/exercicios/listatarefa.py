tarefas = []

# sempre montar a estrutura antes de definir as funções

def adicionarTarefa():
    tarefa = input("\nDigite a nova tarefa: ")

    if tarefa:
        tarefas.append(tarefa)
        print("\nTarefa adicionada com sucesso!\n")

    else:
        print("\nTarefa não pode ser vazia.\n")

def listarTarefas():
    if tarefa:
        print("\nLista de tarefas:\n")
        indice = 1
        
        for tarefa in tarefas:
            print(f"{indice}. {tarefa}")
            indice += 1
    else:
        print("\nNenhuma tarefa cadastrada.\n")

def removerTarefa():
    nome = input("\nDigite o nome da tarefa que deseja remover:")
    if nome in tarefas:
        tarefas.remove(nome)
        print("\nTarefa removida com sucesso!\n")
    else:
        print("\nTarefa não encontrada.\n")

def main():
    while True:
        print("\nMenu de Tarefas\n")
        print("1. Adicionar uma nova tarefa")
        print("2. Listar todas as tarefas")
        print("3. Remover uma terefa pelo nome")
        print("4. Sair")
        opcao = input("\nEscolha uma opção [1-4]:")
        if opcao == "1":
            adicionarTarefa()
        elif opcao == "2":
            listarTarefas()
        elif opcao == "3":
            removerTarefa()
        elif opcao == "4":
            print("\nEncerrando o programam! Ate mais.")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")
    



if __name__ == "__main__":
    main()

