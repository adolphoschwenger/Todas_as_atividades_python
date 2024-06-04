# Dicionário para armazenar os contatos
agenda = {}

# Função para adicionar um contato
def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

# Função para remover um contato
def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para buscar um contato
def buscar_contato(nome):
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

# Função para listar todos os contatos
def listar_contatos():
    if agenda:
        print("Agenda Telefônica:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Agenda vazia.")

# Função principal para o menu
def menu():
    while True:
        print("\nMenu da Agenda Telefônica")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Listar contatos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato a ser buscado: ")
            buscar_contato(nome)
        elif escolha == '4':
            listar_contatos()
        elif escolha == '5':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()