# Bem vindos ao sistema de gerenciamento de contatos de Eduarda Elisa
print("Bem vindo à Lista de Contatos de Eduarda Elisa da silva Oliveira RU: 4876813")  
print("-" * 55)

# Lista para armazenar os contatos
lista_contatos = []  

# Variável para controle do ID global, definido pelo RU 
id_global = 4876813  

# Função para exibir o menu principal
def exibir_menu_principal():
    print("---------------- MENU PRINCIPAL ----------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    print("-" * 55)

# Função para exibir o menu de cadastro
def exibir_menu_cadastrar():
    print("\n---------------- MENU CADASTRAR CONTATO ----------------")
    print(f"Id do Contato: {id_global}")
    print("-" * 55)

# Função para exibir o menu de consulta
def exibir_menu_consultar():
    print("\n---------------- MENU CONSULTAR CONTATO ----------------")
    print("1. Consultar Todos")
    print("2. Consultar por Id")
    print("3. Consultar por Atividade")
    print("4. Retornar ao menu")
    print("-" * 55)

# Função para cadastrar um novo contato
def cadastrar_contato(id):  
    exibir_menu_cadastrar()
    # Pergunta dados do contato
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")

    # Cria o dicionário com as informações do contato
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    # Copia o dicionário para a lista de contatos
    lista_contatos.append(contato.copy())
    print("Contato cadastrado com sucesso!")

# Função para consultar contatos
def consultar_contatos():  
    while True:
        exibir_menu_consultar()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Consultar todos os contatos
            print("\n---------------- TODOS OS CONTATOS ----------------")
            if lista_contatos:
                for contato in lista_contatos:
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
            else:
                print("Nenhum contato cadastrado.")
        elif opcao == "2":
            # Consultar por Id
            id_consulta = int(input("Informe o Id do contato: "))
            encontrado = False
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contato não encontrado.")
        elif opcao == "3":
            # Consultar por Atividade
            atividade_consulta = input("Informe a atividade: ")
            encontrados = [contato for contato in lista_contatos if contato['atividade'] == atividade_consulta]
            if encontrados:
                for contato in encontrados:
                    print(f"ID: {contato['id']}, Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
            else:
                print("Nenhum contato encontrado com essa atividade.")
        elif opcao == "4":
            # Retornar ao menu
            return
        else:
            print("Opção inválida.")

# Função para remover um contato
def remover_contato():  
    while True:
        id_remover = int(input("Informe o Id do contato a ser removido: "))
        for contato in lista_contatos:
            if contato['id'] == id_remover:
                lista_contatos.remove(contato)
                print("Contato removido com sucesso!")
                return
        print("Id inválido. Tente novamente.")

# Menu principal do programa
while True:  
    exibir_menu_principal()
    
    opcao = input(">> ")

    if opcao == "1":
        id_global += 1
        cadastrar_contato(id_global)
    elif opcao == "2":
        consultar_contatos()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")

# EXIGÊNCIAS DE SAÍDA DE CONSOLE

#  Inserir seu próprio cadastro (com meu nome completo, atividade 'estudante' e meu RU)
print("\n--- Exemplo de Cadastro ---")
cadastrar_contato(123456789)  

#  Inserir mais dois contatos com a mesma atividade
cadastrar_contato(123456790)  
cadastrar_contato(123456791)  

#  Consultar todos os contatos cadastrados
print("\n--- Consulta de Todos os Contatos ---")
consultar_contatos()

#  Consultar por Id 
print("\n--- Consulta por Id ---")
consultar_contatos()

#  Consultar por Atividade 
print("\n--- Consulta por Atividade ---")
consultar_contatos()

#  Remover um contato (exemplo: removendo João da Silva) e consultar todos novamente para confirmar remoção
print("\n--- Remoção de Contato ---")
remover_contato()
consultar_contatos()
