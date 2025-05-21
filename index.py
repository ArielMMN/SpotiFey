menu = {
    1: "Cadastrar Usuário",
    2: "Login do usuário",
    0: "Sair"
}

usuario_logado = False  # Indica se há um usuário logado no momento
musicas_curtidas = {}   # Dicionário para armazenar músicas curtidas por usuário
musicas_descurtidas = {} # Dicionário para músicas descurtidas por usuário
nome_usuario_logado = None  # Guarda o nome do usuário logado

def main():
    # Loop principal do programa que exibe o menu e executa ações conforme escolha
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
    # Exibe o menu principal para o usuário e retorna a opção escolhida
    print("Menu:")
    print("----------")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: "))  # Pega a escolha do usuário sem validação
    return escolha

def cadastrar_usuario():
    # Solicita dados para criar um novo usuário e salva no arquivo usuarios.txt
    print("Novo Usuário:")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite o a senha: ")
    with open("usuarios.txt", "a") as arquivo_usuario:
        arquivo_usuario.write(f"{nome},{email},{senha}\n")  # Salva dados separados por vírgula
    print()
    print("Usuário Cadastrado com Sucesso!")
    print()

def login_usuario():
    # Solicita dados para login, verifica se usuário existe no arquivo e autentica
    global usuario_logado
    global nome_usuario_logado

    print()
    print("Logar Usuário:")
    print()
    nome_procurar = input("Nome:")
    email_procurar = input("Email:")
    senha_procurar = input("Senha:")

    with open("usuarios.txt", "r") as arquivo_usuario:
        conteudo = arquivo_usuario.readlines()

    for linha in conteudo:
        nome, email, senha = linha.strip().split(",")
        # Confere se os dados informados correspondem a um usuário cadastrado
        if (nome_procurar.lower() == nome.lower() and
            email_procurar.lower() == email.lower() and
            senha_procurar == senha):
            usuario_logado = True
            nome_usuario_logado = nome
            print()
            print(f"Nome: {nome} | E-mail: {email}")
            print("Usuário logado")
            print()
            menu_log()
            break
    else:
        print("Usuário não encontrado ou dados incorretos.")

menu_logado = {
    1: "Buscar Músicas",
    2: "Curtir música",
    3: "Descurtir música",
    4: "Gerenciar playlists",
    5: "Visualizar histórico",
    0: "Sair"
}

def menu_log():
    # Menu exibido para usuário autenticado com opções para interação musical
    while True: 
        escolha = exibir_menu_logado()
        print()
        if escolha == 1:
            buscar_musica()
        elif escolha == 2:
            curtir_musica()
        elif escolha == 3:
            descurtir_musica()
        elif escolha == 4:
            menu_play()
        elif escolha == 5:
            visualizar_historico()
        elif escolha == 0:
            print("Saindo do Spotifei...")
            break
        else:
            print("Opção Indisponível.")

def exibir_menu_logado():
    # Exibe o menu para usuário logado e retorna a opção escolhida
    print("Menu:")
    print("----------")
    for opcao, descricao in menu_logado.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha

def buscar_musica():
    # Permite buscar uma música pelo nome no arquivo musicas.txt e exibe seus dados
    print()
    print("Buscar Música:")
    print()
    nome_procurar = input("Nome:")
    print()
    with open("musicas.txt", "r") as arquivo_musica:
        conteudo = arquivo_musica.readlines()
    for linha in conteudo:
        nome_musica, nome_artista, duracao = linha.strip().split(",")
        if nome_procurar.lower() == nome_musica.lower():
            print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}")
            print()
            break
    else:
        print("Música não encontrada.")
        print()

def curtir_musica():
    # Permite ao usuário logado curtir uma música existente no banco
    global usuario_logado
    if usuario_logado:
        print()
        print("Curtir Música!")
        print()
        nome_procurar = input("Nome da Música: ")
        print()
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}")
                print()
                resposta = input("Deseja curtir essa música? [s/n]: ")
                if resposta.lower() == "s":
                    if nome_usuario_logado not in musicas_curtidas:
                        musicas_curtidas[nome_usuario_logado] = set()
                    if nome_musica in musicas_curtidas[nome_usuario_logado]:
                        print()
                        print("Música já curtida!")
                        print()
                    else:
                        musicas_curtidas[nome_usuario_logado].add(nome_musica)
                        print()
                        print("Música curtida com sucesso!")
                        print()
                else:
                    print()
                    print("Ok, não curtida.")
                    print()
                encontrado = True
                break

        if not encontrado:
            print()
            print("Música não encontrada.")
            print()

def descurtir_musica():
    # Permite ao usuário logado descurtir uma música existente no banco
    global usuario_logado
    if usuario_logado:
        print()
        print("Descurtir Música!")
        print()
        nome_procurar = input("Nome da Música: ")
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print()
                print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}")
                print()
                resposta = input("Deseja descurtir essa música? [s/n]: ")
                print()
                if resposta.lower() == "s":
                    if nome_usuario_logado not in musicas_descurtidas:
                        musicas_descurtidas[nome_usuario_logado] = set()
                    if nome_musica in musicas_descurtidas[nome_usuario_logado]:
                        print("Música já descurtida!")
                        print()
                    else:
                        musicas_descurtidas[nome_usuario_logado].add(nome_musica)
                        print("Música descurtida com sucesso!")
                        print()
                else:
                    print("Ok, não descurtida.")
                    print()
                encontrado = True
                break

        if not encontrado:
            print("Música não encontrada.")
            print()

menu_playlist = {
    1: "Criar playlists",
    2: "Excluir playlists",
    3: "Adicionar música na playlist",
    4: "Remover música na playlist",
    5: "Visualizar playlists",
    0: "Sair"
}

def menu_play():
    # Menu para gerenciar playlists do usuário logado
    while True:
        escolha = exibir_menu_play()
        print()
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

def exibir_menu_play():
    # Exibe o menu de playlists e retorna a escolha do usuário
    print("Menu:")
    print("----------")
    for opcao, descricao in menu_playlist.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha

def criar_play():
    # Cria uma nova playlist associada ao usuário logado
    global nome_usuario_logado
    print("Nova playlist:")
    print()
    nome_playlist = input("Digite o nome: ")
    print()
    with open("playlists.txt", "a") as arquivo_playlist:
        arquivo_playlist.write(f"{nome_usuario_logado},{nome_playlist}\n")
    print("Playlist criada com sucesso!")
    print()

def excluir_play():
    # Exclui uma playlist pelo nome, removendo a linha correspondente do arquivo
    nome_apagar = input("Digite o nome do play que deseja apagar: ")
    print()
    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    # Procura e remove a playlist com o nome informado
    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue
        nome_usuario, nome_playlist = partes[0], partes[1]
        if nome_apagar.lower() == nome_playlist.lower():
            conteudo.pop(i)
            print("Playlist removida com sucesso.")
            print()
            break
    else:
        print("Playlist não encontrada.")
        print()

    with open("playlists.txt", "w") as arquivo_playlist:
        arquivo_playlist.writelines(conteudo)

def add_musica_play():
    # Adiciona uma música a uma playlist existente do usuário logado
    global nome_usuario_logado
    print("Adicionar música à playlist:")
    print()
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja adicionar: ").strip()
    print()

    # Verifica se a música existe no banco de músicas
    with open("musicas.txt", "r") as arquivo_musica:
        musicas_disponiveis = [linha.strip().split(",")[0].lower() for linha in arquivo_musica]

    if nome_musica.lower() not in musicas_disponiveis:
        print("Música não encontrada no banco de músicas.")
        print()
        return

    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    # Procura a playlist do usuário logado e adiciona a música
    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue
        nome_usuario, nome_playlist_arquivo = partes[0], partes[1]
        if nome_usuario == nome_usuario_logado and nome_playlist_arquivo.lower() == nome_playlist.lower():
            # Se a música já está na playlist, não adiciona novamente
            if nome_musica in partes[2:]:
                print("Música já está na playlist.")
                print()
                return
            conteudo[i] = linha.strip() + f",{nome_musica}\n"
            with open("playlists.txt", "w") as arquivo_playlist:
                arquivo_playlist.writelines(conteudo)
            print("Música adicionada com sucesso!")
            print()
            return

    print("Playlist não encontrada.")
    print()

def remove_musica_play():
    # Remove uma música de uma playlist existente do usuário logado
    global nome_usuario_logado
    print("Remover música da playlist:")
    print()
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja remover: ").strip()
    print()

    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue
        nome_usuario, nome_playlist_arquivo = partes[0], partes[1]
        if nome_usuario == nome_usuario_logado and nome_playlist_arquivo.lower() == nome_playlist.lower():
            if nome_musica in partes[2:]:
                partes.remove(nome_musica)
                conteudo[i] = ",".join(partes) + "\n"
                with open("playlists.txt", "w") as arquivo_playlist:
                    arquivo_playlist.writelines(conteudo)
                print("Música removida com sucesso!")
                print()
                return
            else:
                print("Música não encontrada na playlist.")
                print()
                return

    print("Playlist não encontrada.")
    print()

def visualizar_play():
    # Mostra todas as playlists do usuário logado e as músicas que elas contêm
    global nome_usuario_logado
    print(f"Playlists do usuário {nome_usuario_logado}:")
    print()
    with open("playlists.txt", "r") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

    encontrou = False
    for linha in conteudo:
        partes = linha.strip().split(",")
        if len(partes) < 2:
            continue
        nome_usuario, nome_playlist = partes[0], partes[1]
        if nome_usuario == nome_usuario_logado:
            encontrou = True
            musicas = partes[2:]
            print(f"Playlist: {nome_playlist}")
            if musicas:
                print("Músicas:")
                for m in musicas:
                    print(f" - {m}")
            else:
                print("Playlist vazia.")
            print()

    if not encontrou:
        print("Você não possui playlists cadastradas.")
        print()

def visualizar_historico():
    # Apenas um placeholder que poderia mostrar um histórico de músicas tocadas
    print("Funcionalidade de histórico ainda não implementada.")
    print()

if __name__ == "__main__":
    main()
