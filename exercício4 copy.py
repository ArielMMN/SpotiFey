# Menu principal é um dicionario onde onde exibe caba valor
menu = {
    1: "Cadastrar Usuário",
    2: "Login do usuário",
    0: "Sair"
}

usuario_logado = False
musicas_curtidas = {}
musicas_descurtidas = {}

def main():
    while True: 
        escolha = exibir_menu()
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            login_usuario()  
        elif escolha == 0:
            print("Saindo do Spotifei...")
            break
        else:
            print("Opção Indisponível.")

def exibir_menu():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida


def cadastrar_usuario():
    """
    Função para cadastrar um novo contato à agenda.
    """
    print("Novo Usuário:")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite o a senha: ")
    # Abre o arquivo contatos.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_usuario = open("usuarios.txt", "a")
    # Grava o contato no arquivo
    arquivo_usuario.write(f"{nome},{email},{senha}\n") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_usuario.close()
    print("Usuário Cadastrado com Sucesso!") # Mensagem de sucesso

def login_usuario():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    global usuario_logado
    print("Logar Usuário:")
    nome_procurar = input("Nome:")
    email_procurar = input("Email:")
    senha_procurar = input("Senha:")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("usuarios.txt", "r") as arquivo_usuario:
        conteudo = arquivo_usuario.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome, email, senha= linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_procurar.lower() == nome.lower() and email_procurar.lower() == email.lower() and senha_procurar.lower() == senha.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            usuario_logado = True
            print(usuario_logado)
            print(f"Nome: {nome}, E-mail: {email}")
            print("Usuario logado")
            menu_log()
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Contato não encontrado.") # Mensagem de erro se o contato não for encontrado

menu_logado = {
    1: "Buscar Músicas",
    2: "Curtir música",
    3: "Descurtir música",
    4: "Visualizar histórico",
    0: "Sair"
}

def menu_log():
    while True: 
        escolha = exibir_menu_logado()
        if escolha == 1:
            buscar_musica()
        elif escolha == 2:
            curtir_musica()
        elif escolha == 3:
            descurtir_musica()
        elif escolha == 4:
            visualizar_historico()
        elif escolha == 0:
            print("Saindo do Spotifei...")
            break
        else:
            print("Opção Indisponível.")


def exibir_menu_logado():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu_logado.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def buscar_musica():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """

    print("Buscar Musica:")
    nome_procurar = input("Nome:")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("musicas.txt", "r") as arquivo_musica:
        conteudo = arquivo_musica.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome_musica, nome_artista, duracao = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_procurar.lower() == nome_musica.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Nome: {nome_musica}, Artista: {nome_artista}, , Duração: {duracao}")
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Musica não encontrado.") # Mensagem de erro se o contato não for encontrado

def curtir_musica():
    global usuario_logado
    if usuario_logado:
        print("Curtir Música!")
        nome_procurar = input("Nome da Música: ")
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}")
                resposta = input("Deseja curtir essa música? [s/n]: ")
                if resposta == "s":
                    if usuario_logado not in musicas_curtidas:
                        musicas_curtidas[usuario_logado] = set()  # cria conjunto vazio

                    if nome_musica in musicas_curtidas[usuario_logado]:
                        print("Música já curtida!")
                    else:
                        musicas_curtidas[usuario_logado].add(nome_musica)
                        print("Música curtida com sucesso!")
                else:
                    print("Ok, não curtida.")
                encontrado = True
                break

        if not encontrado:
            print("Música não encontrada.")


def descurtir_musica():
    global usuario_logado
    if usuario_logado:
        print("Descurtir Música!")
        nome_procurar = input("Nome da Música: ")
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}")
                resposta = input("Deseja descurtir essa música? [s/n]: ")
                if resposta == "s":
                    if usuario_logado not in musicas_descurtidas:
                        musicas_curtidas[usuario_logado] = set()  # cria conjunto vazio

                    if nome_musica in musicas_descurtidas[usuario_logado]:
                        print("Música já descurtir!")
                    else:
                        musicas_descurtidas[usuario_logado].add(nome_musica)
                        print("Música descurtir com sucesso!")
                else:
                    print("Ok, não descurtir.")
                encontrado = True
                break

        if not encontrado:
            print("Música não encontrada.")


def visualizar_historico():
    escolha = str(input("Visualizar musicas curtidas(C) ou descurtidas(D): "))
    if escolha == "C":
        listar_musicas_curtidas()
    else:
        listar_musicas_descurtidas()

def listar_musicas_curtidas():
    global usuario_logado
    if usuario_logado:
        if usuario_logado in musicas_curtidas and musicas_curtidas[usuario_logado]:
            print("Músicas curtidas:")
            for musica in musicas_curtidas[usuario_logado]:
                print(f"- {musica}")
        else:
            print("Você ainda não curtiu nenhuma música.")

def listar_musicas_descurtidas():
    global usuario_logado
    if usuario_logado:
        if usuario_logado in musicas_descurtidas and musicas_descurtidas[usuario_logado]:
            print("Músicas descurtida:")
            for musica in musicas_descurtidas[usuario_logado]:
                print(f"- {musica}")
        else:
            print("Você ainda não descurtida nenhuma música.")

if __name__ == "__main__":
    main()
