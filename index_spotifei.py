# Dicionário com o menu principal (antes do login)
menu = {
    1: "Cadastrar Usuário",
    2: "Login do usuário",
    0: "Sair"
}

# Variáveis globais
usuario_logado = False  # Indica se há um usuário logado
musicas_curtidas = {}  # Dicionário com músicas curtidas por usuário
musicas_descurtidas = {}  # Dicionário com músicas descurtidas por usuário
nome_usuario_logado = None  # Guarda o nome do usuário logado

# Função principal que controla o fluxo do programa
def main():
    while True:  # Loop infinito até o usuário escolher sair
        escolha = exibir_menu()
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            login_usuario()  
        elif escolha == 0:
            print("Saindo do Spotifei...")
            break  # Sai do loop e termina o programa
        else:
            print("Opção Indisponível.")

# Mostra o menu principal e retorna a escolha do usuário
def exibir_menu():
    print("Menu:")
    print("----------")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha

# Cadastra um novo usuário e salva no arquivo
def cadastrar_usuario():
    print("Novo Usuário:")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite o a senha: ")
    arquivo_usuario = open("usuarios.txt", "a")  # Abre o arquivo no modo adicionar
    arquivo_usuario.write(f"{nome},{email},{senha}\n")
    arquivo_usuario.close()
    print("\nUsuário Cadastrado com Sucesso!\n")

# Realiza o login do usuário, verificando os dados no arquivo
def login_usuario():
    global usuario_logado
    global nome_usuario_logado
    print("\nLogar Usuário:\n")
    nome_procurar = input("Nome:")
    email_procurar = input("Email:")
    senha_procurar = input("Senha:")
    with open("usuarios.txt", "r") as arquivo_usuario:
        conteudo = arquivo_usuario.readlines()
    
    # Verifica se os dados batem com algum cadastro
    for linha in conteudo:
        nome, email, senha = linha.strip().split(",")
        if nome_procurar.lower() == nome.lower() and email_procurar.lower() == email.lower() and senha_procurar.lower() == senha.lower():
            usuario_logado = True
            nome_usuario_logado = nome
            print(f"\nNome: {nome} | E-mail: {email}\nUsuario logado\n")
            menu_log()  # Chama o menu de usuário logado
            break
    else:
        print("Contato não encontrado.")

# Menu exibido após o login
menu_logado = {
    1: "Buscar Músicas",
    2: "Curtir música",
    3: "Descurtir música",
    4: "Gerenciar playlists",
    5: "Visualizar histórico",
    0: "Sair"
}

# Mostra o menu de usuário logado e trata as opções
def menu_log():
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

# Exibe o menu do usuário logado
def exibir_menu_logado():
    print("Menu:")
    print("----------")
    for opcao, descricao in menu_logado.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: ")) 
    return escolha 

# Permite buscar uma música pelo nome
def buscar_musica():
    print("\nBuscar Musica:\n")
    nome_procurar = input("Nome:")
    print()
    with open("musicas.txt", "r") as arquivo_musica:
        conteudo = arquivo_musica.readlines()
    
    for linha in conteudo:
        nome_musica, nome_artista, duracao = linha.strip().split(",")
        if nome_procurar.lower() == nome_musica.lower():
            print(f"Nome: {nome_musica}, Artista: {nome_artista}, , Duração: {duracao}\n")
            break
    else:
        print("Musica não encontrada.\n")

# Permite o usuário curtir uma música
def curtir_musica():
    global usuario_logado
    if usuario_logado:
        print("\nCurtir Música!\n")
        nome_procurar = input("Nome da Música: ")
        print()
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print(f"Nome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}\n")
                resposta = input("Deseja curtir essa música? [s/n]: ")
                if resposta == "s":
                    if usuario_logado not in musicas_curtidas:
                        musicas_curtidas[usuario_logado] = set()
                    if nome_musica in musicas_curtidas[usuario_logado]:
                        print("\nMúsica já curtida!\n")
                    else:
                        musicas_curtidas[usuario_logado].add(nome_musica)
                        print("\nMúsica curtida com sucesso!\n")
                else:
                    print("\nOk, não curtida.\n")
                encontrado = True
                break

        if not encontrado:
            print("\nMúsica não encontrada.\n")

# Permite o usuário descurtir uma música
def descurtir_musica():
    global usuario_logado
    if usuario_logado:
        print("\nDescurtir Música!\n")
        nome_procurar = input("Nome da Música: ")
        encontrado = False

        with open("musicas.txt", "r") as arquivo_musica:
            conteudo = arquivo_musica.readlines()

        for linha in conteudo:
            nome_musica, nome_artista, duracao = linha.strip().split(",")
            if nome_procurar.lower() == nome_musica.lower():
                print(f"\nNome: {nome_musica}, Artista: {nome_artista}, Duração: {duracao}\n")
                resposta = input("Deseja descurtir essa música? [s/n]: ")
                if resposta == "s":
                    if usuario_logado not in musicas_descurtidas:
                        musicas_descurtidas[usuario_logado] = set()
                    if nome_musica in musicas_descurtidas[usuario_logado]:
                        print("Música já descurtida!\n")
                    else:
                        musicas_descurtidas[usuario_logado].add(nome_musica)
                        print("Música descurtida com sucesso!\n")
                else:
                    print("Ok, não descurtida.\n")
                encontrado = True
                break

        if not encontrado:
            print("Música não encontrada.\n")

# Menu de gerenciamento de playlists
menu_playlist = {
    1: "Criar playlists",
    2: "Excluir playlists",
    3: "Adicionar música na playlists",
    4: "Remover música na playlists",
    5: "Visualizar playlists",
    0: "Sair"
}

# Exibe e trata opções do menu de playlists
def menu_play():
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

# Exibe o menu de playlists
def exibir_menu_play():
    print("Menu:")
    print("----------")
    for opcao, descricao in menu_playlist.items():
        print(f"{opcao} - {descricao}")
    print()
    escolha = int(input("Escolha uma opção: "))
    return escolha 

# Cria uma nova playlist
def criar_play():
    global nome_usuario_logado
    print("Nova playlist:\n")
    nome_playlist = input("Digite o nome: ")
    print()
    arquivo_playlist = open("playlists.txt", "a")
    arquivo_playlist.write(f"{nome_usuario_logado},{nome_playlist}\n")
    arquivo_playlist.close()
    print("Playlist criada com sucesso!\n")

def excluir_play():

    nome_apagar = input("Digite o nome da playlist que deseja apagar: ")
    print()


    with open("playlists.txt", "r", encoding="utf-8") as arquivo_playlist:
        conteudo = arquivo_playlist.readlines()

 
    encontrou = False


    for i, linha in enumerate(conteudo):
        partes = linha.strip().split(",")  
        if len(partes) > 1 and nome_apagar.lower() == partes[1].lower():
            print(f"Playlist encontrada: {linha.strip()}")
            print()
            conteudo.pop(i)  
            encontrou = True
            break

    if encontrou:
        with open("playlists.txt", "w", encoding="utf-8") as arquivo_playlist:
            arquivo_playlist.writelines(conteudo)
        print("Playlist removida com sucesso.")
        print()
    else:
        print("Playlist não encontrada.")
        print()

def add_musica_play():
    global nome_usuario_logado
    print("Adicionar música à playlist:")
    print()
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja adicionar: ").strip()
    print()

    # Verifica se a música existe em musicas.txt
    with open("musicas.txt", "r") as arquivo_musica:
        musicas_disponiveis = [linha.strip().split(",")[0].lower() for linha in arquivo_musica]

    if nome_musica.lower() not in musicas_disponiveis:
        print("Música não encontrada no banco de músicas.")
        print()
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
                print()
            else:
                musicas.append(nome_musica)
                conteudo[i] = f"{nome_usuario},{playlist}," + ",".join(musicas) + "\n"
                print("Música adicionada com sucesso.")
                print()
            break
    else:
        print("Playlist não encontrada ou você não é o dono.")
        print()

    # Salva a playlist atualizada
    with open("playlists.txt", "w") as arquivo:
        arquivo.writelines(conteudo)


def remove_musica_play():
    global nome_usuario_logado
    print("Remover música da playlist:")
    print()
    nome_playlist = input("Digite o nome da playlist: ").strip()
    nome_musica = input("Digite o nome da música que deseja remover: ").strip()
    print()

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
                print()
            else:
                print("A música não está na playlist.")
                print()
            break
    else:
        print("Playlist não encontrada ou você não é o dono.")
        print()

    # Salva a playlist atualizada
    with open("playlists.txt", "w") as arquivo:
        arquivo.writelines(conteudo)

def visualizar_play():
    global nome_usuario_logado
    print("Buscar playlist:")
    print()
    nome_procurar = input("Digite o nome da playlist: ").strip()
    print()

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
            print()
            if musicas:
                print("Músicas:")
                print()
                for musica in musicas:
                    print(f"- {musica}")
            else:
                print("Essa playlist está vazia.")
                print()
            encontrada = True
            break

    if not encontrada:
        print("Playlist não encontrada ou não pertence a você.")
        print()

def visualizar_historico():
    while True:  # Colocar o menu dentro do loop para repetir após cada ação
        print("\nVisualizar Histórico:")
        print("1 - Visualizar músicas curtidas")
        print("2 - Visualizar músicas descurtidas")
        print("0 - Voltar")
        
        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue  # Volta para o menu

        if escolha == 1:
            listar_musicas_curtidas()
        elif escolha == 2:
            listar_musicas_descurtidas()
        elif escolha == 0:
            print("Voltando...")
            print()
            break
        else:
            print("Opção indisponível.")

def listar_musicas_curtidas():
    global usuario_logado
    if usuario_logado:
        if usuario_logado in musicas_curtidas and musicas_curtidas[usuario_logado]:
            print("\nMúsicas curtidas:")
            for musica in musicas_curtidas[usuario_logado]:
                print(f"- {musica}")
        else:
            print("\nVocê ainda não curtiu nenhuma música.")
    else:
        print("\nNenhum usuário logado.")

def listar_musicas_descurtidas():
    global usuario_logado
    if usuario_logado:
        if usuario_logado in musicas_descurtidas and musicas_descurtidas[usuario_logado]:
            print("\nMúsicas descurtidas:")
            for musica in musicas_descurtidas[usuario_logado]:
                print(f"- {musica}")
        else:
            print("\nVocê ainda não descurtiu nenhuma música.")
    else:
        print("\nNenhum usuário logado.")

if __name__ == "__main__":
    main()