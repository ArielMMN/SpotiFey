menu = {
    1: "Cadastrar Usuário",
    2: "Login do usuário",
    0: "Sair"
}

usuario_logado = False
musicas_curtidas = {}
musicas_descurtidas = {}
nome_usuario_logado = None

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
    global nome_usuario_logado
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
            nome_usuario_logado = nome
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
    4: "Gerenciar playlists",
    5: "Visualizar histórico",
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
            gerenciar_playlists()
        elif escolha == 5:
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
                resposta = input("Deseja descurtir essa música? [S/N]: ")
                if resposta == "S":
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

def gerenciar_playlists():
    while True:
        print("Gerenciar Playlist:")
        print("1 - Criar playlist")
        print("2 - Excluir playlist")
        print("3 - Adicionar música")
        print("4 - Remover música")
        print("5 - Ver playlists")
        print("0 - Voltar")
        escolha = int(input("Escolha: "))
        if escolha == 1:
            criar_play()
        elif escolha == 2:
            excluir_play()
        elif escolha == 3:
            add_musica_play()
        elif escolha == 4:
            remove_musica_play()
        elif escolha == 5:
            visualizar_play()
        elif escolha == 0:
            print("Voltando...")
            break
        else:
            print("Opção Indisponível.")


def criar_play():
    """
    Função para cadastrar um novo contato à agenda.
    """
    global nome_usuario_logado
    print("Nova playlist:")
    nome_playlist = input("Digite o nome: ")
    # Abre o arquivo contatos.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_playlist = open("playlists.txt", "a")
    # Grava o contato no arquivo
    arquivo_playlist.write(f"{nome_usuario_logado},{nome_playlist}") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_playlist.close()
    print("Playlist") # Mensagem de sucesso

def excluir_play():
    """
    Apaga um contato da agenda.
    :return: None
    """
    nome_apagar = input("Digite o nome do play que deseja apagar: ")
    # Abre o arquivo contatos.txt para leitura
    arquivo_playlist = open("playlists.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_playlist.readlines()
    # Fecha o arquivo
    arquivo_playlist.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo):
        nome = linha.strip().split(",")
        if nome_apagar.lower() == nome.lower():
            print(f"Contato encontrado: {linha.strip()}")
            # Remove o contato da lista
            conteudo.pop(i)
            break
    else: # Se não encontrar o contato
        print("play não encontrado.")

def add_musica_play():
    global nome_usuario_logado
    print("Adicionar música à playlist:")
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja adicionar: ").strip()

    # Verifica se a música existe em musicas.txt
    with open("musicas.txt", "r") as arquivo_musica:
        musicas_disponiveis = [linha.strip().split(",")[0].lower() for linha in arquivo_musica]

    if nome_musica.lower() not in musicas_disponiveis:
        print("Música não encontrada no banco de músicas.")
        return

    # Lê as playlists
    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    # Procura a playlist do usuário logado
    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue

        nome_usuario, playlist = partes[0], partes[1]
        musicas = partes[2:]

        if nome_usuario == nome_usuario_logado and playlist == nome_playlist:
            if nome_musica in musicas:
                print("A música já está na playlist.")
            else:
                musicas.append(nome_musica)
                conteudo[i] = f"{nome_usuario},{playlist}," + ",".join(musicas) + "\n"
                print("Música adicionada com sucesso.")
            break
    else:
        print("Playlist não encontrada ou você não é o dono.")

    # Salva a playlist atualizada
    with open("playlists.txt", "w") as arquivo:
        arquivo.writelines(conteudo)


def remove_musica_play():
    global nome_usuario_logado
    print("Remover música da playlist:")
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja remover: ").strip()

    # Lê as playlists
    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    # Procura a playlist do usuário logado
    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue

        nome_usuario, playlist = partes[0], partes[1]
        musicas = partes[2:]

        if nome_usuario == nome_usuario_logado and playlist == nome_playlist:
            if nome_musica in musicas:
                musicas.remove(nome_musica)
                conteudo[i] = f"{nome_usuario},{playlist}," + ",".join(musicas) + "\n"
                print("Música removida com sucesso.")
            else:
                print("A música não está na playlist.")
            break
    else:
        print("Playlist não encontrada ou você não é o dono.")

    # Salva a playlist atualizada
    with open("playlists.txt", "w") as arquivo:
        arquivo.writelines(conteudo)

def visualizar_play():
    global nome_usuario_logado
    print("Buscar playlist:")
    nome_procurar = input("Digite o nome da playlist: ").strip()

    encontrada = False

    with open("playlists.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        partes = linha.strip().split(",")

        if len(partes) < 2:
            continue

        nome_usuario = partes[0]
        nome_playlist = partes[1]
        musicas = partes[2:]

        if nome_usuario == nome_usuario_logado and nome_playlist.lower() == nome_procurar.lower():
            print(f"\nPlaylist: {nome_playlist}")
            if musicas:
                print("Músicas:")
                for musica in musicas:
                    print(f"- {musica}")
            else:
                print("Essa playlist está vazia.")
            encontrada = True
            break

    if not encontrada:
        print("Playlist não encontrada ou não pertence a você.")

def visualizar_historico():
    print("Visualizar Historico:")
    print("1 - Visualizar musicas curtidas")
    print("2 - Visualizar musicas Descurtidas")
    print("0 - voltar")
    escolha = int(input("Escolha: "))
    while True:
        if escolha == 1:
            listar_musicas_curtidas()
        elif escolha == 2:
            listar_musicas_descurtidas()
        elif escolha == 0:
            print("Voltando")
            break
        else:
            print("Opção Indisponível.")
        

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
