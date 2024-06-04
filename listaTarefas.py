# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(descricao):
    tarefas.append({"descricao": descricao, "concluida": False})
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

# Função para remover uma tarefa
def remover_tarefa(index):
    try:
        tarefa = tarefas.pop(index)
        print(f"Tarefa '{tarefa['descricao']}' removida com sucesso!")
    except IndexError:
        print("Índice inválido. Por favor, tente novamente.")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(index):
    try:
        tarefas[index]["concluida"] = True
        print(f"Tarefa '{tarefas[index]['descricao']}' marcada como concluída!")
    except IndexError:
        print("Índice inválido. Por favor, tente novamente.")

# Função para listar todas as tarefas
def listar_tarefas():
    if tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")
    else:
        print("Nenhuma tarefa na lista.")

# Função principal para o menu
def menu():
    while True:
        print("\nMenu da Lista de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Concluir tarefa")
        print("4. Listar tarefas")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif escolha == '2':
            try:
                index = int(input("Digite o índice da tarefa a ser removida: "))
                remover_tarefa(index)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == '3':
            try:
                index = int(input("Digite o índice da tarefa a ser concluída: "))
                concluir_tarefa(index)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == '4':
            listar_tarefas()
        elif escolha == '5':
            print("Saindo da lista de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()