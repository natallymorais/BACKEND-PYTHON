alunosIA = set()
alunosPython = set()

def adicionarAluno():
    nome = input("Digite o nome do aluno:").strip()
    while nome == "":
        print("\nNome do aluno não pode ser vazio.\n")
        nome = input("Digite o nome do aluno:").strip()
        
    evento = input("Evento que participou (IA OU Python):").strip().lower()
    if evento == "ia":
        alunosIA.add(nome)
        print(f"\n{nome} adicionao á palestra IA.\n")
    elif evento == "python":
        alunosPython.add(nome)
        print(f"\n{nome} adicionao á palestra Workshop Python.\n")
    else:
        print("\nEvento inválido. Digite apenar IA ou Python.\n")
        
def mostrarAmbos():
    ambos = alunosIA.intersection(alunosPython)
    print(f"\nAlunos que participaram de ambos os eventos: \n")
    if ambos:
        for aluno in ambos:
            print(aluno)
    else:
        print("\nNenhum aluno participou de ambos os eventos.\n")
        
def mostrarSomenteIA():
    somenteIa = alunosIA.difference(alunosPython)
    print(f"\nAlunos que participaram somente da palestra de IA: \n")
    if somenteIa:
        for aluno in somenteIa:
            print(aluno)
    else:
        print("\nNenhum aluno participou somente da palestra de IA.\n")

def mostrarAlunos():
    pelomenosUm = alunosIA.union(alunosPython)
    print(f"\nAlunos que participaram de pelo menos um evento: \n")
    if pelomenosUm:
        for aluno in pelomenosUm:
            print(aluno)
    else:
        print("\nNenhum aluno participou de eventos.\n")

def verificarParticipação():
    nome = input("Nome do aluno que deseja verificar:").strip().lower()
    emIa = nome in alunosIA
    emPython = nome in alunosPython
    
    if emIa and emPython:
        print(f"{nome} participou de ambos os eventos.")
    elif emIa:
        print(f"{nome} participou somente da palestra de IA. ")
    elif emPython:
        print(f"{nome} participou somente do Workshop de Python. ")
    else:
        print(f"{nome} não participou de nenhuma palestra. ")

def main():
    while True:
        print("\n--- MENU ---\n")
        print("1. Adicionar aluno a um evento")
        print("2. Mostrtar alunos que participaram de ambos os eventos")
        print("3. Mostrar alunos que participaram somente da palesta de IA")
        print("4. Mostrar alunos que participaram de pelo menos um evento")
        print("5. Verificar participação de um aluno ")
        print("6. Sair ")
        
        opcao = input("\nEscolha uma opção [1-6]\n").strip()
        if opcao == "1":
            adicionarAluno()
        elif opcao == "2":
            mostrarAmbos()
        elif opcao == "3":
            mostrarSomenteIA()
        elif opcao == "4":
            mostrarAlunos()
        elif opcao == "5":
            verificarParticipação()
        elif opcao == "6":
            print("\nEncerrando o programam! Ate mais.")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()