notas = []


def adicionarNota():
        nome = input("\nDigite o nome do aluno:").strip()
        while nome == "":
            print("\nNome não pode estar vazio.\n")
            nome = input("\nDigite o nome do aluno:").strip()
            
        nota = (input("Nota : ")).strip()
        while not nota.replace('.', '').isdigit() or not (0 <= float(nota) <= 10):
            print("\nNota inválida! Digite um número entre o e 10.\n")
            nota = (input("Nota [0 - 10] : ")).strip()
        
        disciplina = (input("Disciplina: ")).strip()
        while disciplina == "":
            print("\Disciplina não pode estar vazio.\n")
            disciplina = (input("Disciplina: ")).strip()
            
        notas.append((nome,nota,disciplina))
        print("\nNota adicionada com sucesso.\n")

def melhorAluno():
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada\n")
        return
    disciplinas = []
    
    for n in notas:
        if n[2] not in disciplinas:
            disciplinas.append(n[2])
            
    print("\nMelhor aluno por disciplina:\n")
    
    for d in disciplinas:
        melhorNota = -1
        melhorAluno = ""
        for n in notas:
            if n[2] == d and float(n[1]) > float(melhorNota):
                melhorNota = n[1]
                melhorAluno = n[0]
        print(f"{d}: {melhorAluno} ({melhorNota})")
    
def consultarNotas():
    nome_busca = input("\nDigite o nome do aluno \n")
    encontrou = False
    
    for n in notas:
        if n[0].lower() == nome_busca.lower():
            encontrou = True
            print(f"{n[2]}: {n[1]}")
    if not encontrou:
        print("\nNenhuma nota encontrada para este aluno\n")
    
def obterNota(tupla):
    return tupla[1]

def exibirNotas():
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada\n")
        return
    ordenadas = sorted(notas, kay=obterNota, reserv=True)
    for 
    
def main():
    while True:
        print("\nCadastrar Notas\n")
        print("1. Adicionar nota")
        print("2. Mostrtar melhor aluno por diciplina")
        print("3. Consultar notas por alunos")
        print("4. Exibir notas ordenadas")
        print("5. Sair")
        opcao = input("\nEscolha uma opção [1-5]\n")
        if opcao == "1":
            adicionarNota()
        elif opcao == "2":
            melhorAluno()
        elif opcao == "3":
            consultarNotas()
        elif opcao == "4":
            exibirNotas()
        elif opcao == "5":
            print("\nEncerrando o programam! Ate mais.")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()