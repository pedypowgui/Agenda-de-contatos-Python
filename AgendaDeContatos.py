contatos =  {}

#Pegar os valores de agenda.txt
try:
    with open("agenda.txt", "r") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()] #Cria lista com as linhas do arquivo
        for i in range(0, len(linhas), 3):
            nome = linhas[i].strip().split(": ")[1].upper()
            tel = linhas[i + 1].strip().split(": ")[1]
            contatos[nome] = tel
#Em caso do arquivo não existir, cria-se um 
except FileNotFoundError:
    open("agenda.txt", "w").close()



#Imprimir a lista com todos os contatos
def listarContatos():
    if not contatos:
        print("\nNenhum contato encontrado.\n")
    for i, j in contatos.items():
        print(f"\nNome: {i.title()}")
        print(f"Telefone: {j}\n")

#Adicionar contato à lista
def adicionarContato(nome, telefone):
    if not nome.strip() or not telefone.strip():
        print("\nERRO: String vazia\n")
    elif not telefone.replace(" ", "").isdigit() or len(telefone.replace(" ", "")) != 11:
        print("\nERRO: Telefone inválido, digite-o no formato \'XX XXXXXXXX\' (11 dígitos com DDD)\n")
    elif nome in contatos:
        print("\nERRO: Contato já existente\n")
    else:
        contatos[nome] = telefone
        print("\nContato adicionado com sucesso!\n")

#Procurar contato através do nome
def procurarContato(chave):
    if chave in contatos:
        print(f"\nNome: {chave.title()}")
        print(f"Telefone: {contatos[chave]}\n")
    else:
        print("\nNome não encontrado\n")

#Procurar algum contato pelo telefone
def procurarTelefone(value):
    for i, j in contatos.items():
        if value == j:
            return f"\nnome: {i.title()}\nTelefone: {j}\n"
    else:
        return "\nTelefone não encontrado\n"

#Remover contato
def removerContato(nome):
    if nome in contatos.keys():
        del contatos[nome]
        print("\nContato removido com sucesso.\n")
    else:
        print("ERRO: Contato não existente\n")

#gravar agenda em agenda.txt
def gravarEmArquivo():
    with open("agenda.txt", "w") as arquivo:
        for user, tel in contatos.items():
            arquivo.write(f"Nome: {user}\n")
            arquivo.write(f"Telefone: {tel}\n")
            arquivo.write(f"----------------------\n")


#Loop de interação com o menu
while True:
    try:
        opc = int(input("[1] - Adicionar contato\n[2] - Pesquisar nome\n[3] - Pesquisar telefone\n[4] - Listar todos os contatos\n[5] - Remover contato\n[0] - Sair\n"))
    except ValueError:
        print("ERRO: Entrada inválida, digite um número.")
        continue
    #Sair do menu de opções
    if opc == 0:
        gravarEmArquivo()
        print("Agenda salva. Saindo...")
        break
    #Adicionar contato
    elif opc == 1:
        nome = input("Digite o nome do contato para adicionar: ")
        telefone = input("Digite o número do contato para adicionar: ")
        
        nome = nome.upper()
        
        adicionarContato(nome, telefone)
        gravarEmArquivo()
    #Pesquisar contato através do nome
    elif opc == 2:
        name = input("Digite o nome do contato a ser procurado: ")
        
        name = name.upper()
        
        procurarContato(name)
    #Pesquisar contato através do telefone
    elif opc == 3:
        tel = input("Digite o telefone do contato a ser procurado: ")
        print(procurarTelefone(tel))
    #Listar todos os contatos
    elif opc == 4:
        listarContatos()
    #Remover contato
    elif opc == 5:
        nome = input("Digite o nome do contato para remover: ")

        nome = nome.upper()
        
        removerContato(nome)
        gravarEmArquivo()
    #Opção inválida
    else:
        print("\nOpção inválida, digite um número de 0 a 5\n")
