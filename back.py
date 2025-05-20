menu = {
    1: "Cadastrar Usuário",
    2: "Login do usuário",
    3: "Buscar Músicas",
    4: "Curtir música",
    5: "Descurtir música",
    6: "Visualizar histórico",
    7: "Músicas curtidas",
    8: "Músicas descurtidas",
    9: "Gerenciar playlists",
    0: "Sair"
}

usuario_logado = False

def main():
    while True: 
        escolha = exibir_menu()
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            login_usuario()
        elif escolha == 3:
            buscar_musica()
        elif escolha == 4:
            curtir_musica()
        elif escolha == 5:
            descurtir_musica()
        elif escolha == 6:
            visualizar_historico()
        elif escolha == 7:
            listar_musicas_curtidas()
        elif escolha == 8:
            listar_musicas_descurtidas()
        elif escolha == 9:
            gerenciar_playlists()
        elif escolha == 0:
            print("Saindo do Spotifei...")
            break
        else:
            print("Opção Indisponível.")


def login_usuario():
    global usuario_logado
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    if usuarios.get(nome) == senha:
        usuario_logado = nome
        print(f"Bem-vindo, {nome}!")
    else:
        print("Usuário ou senha inválidos.")

def buscar_musica():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    nome_musica = input("Digite o nome da música: ")
    print(f"Música encontrada: {nome_musica}")
    historico_buscas.setdefault(usuario_logado, []).append(nome_musica)

def curtir_musica():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    musica = input("Digite o nome da música para curtir: ")
    musicas_curtidas.setdefault(usuario_logado, set()).add(musica)
    print(f"Você curtiu: {musica}")

def descurtir_musica():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    musica = input("Digite o nome da música para descurtir: ")
    musicas_descurtidas.setdefault(usuario_logado, set()).add(musica)
    print(f"Você descurtiu: {musica}")

def listar_musicas_curtidas():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    print("Músicas curtidas:")
    for m in musicas_curtidas.get(usuario_logado, []):
        print(f"- {m}")

def listar_musicas_descurtidas():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    print("Músicas descurtidas:")
    for m in musicas_descurtidas.get(usuario_logado, []):
        print(f"- {m}")

def visualizar_historico():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return
    print("Histórico de buscas:")
    for m in historico_buscas.get(usuario_logado, []):
        print(f"- {m}")

def gerenciar_playlists():
    if not usuario_logado:
        print("Você precisa estar logado.")
        return

    while True:
        print("\nGerenciar Playlist")
        print("1 - Criar playlist")
        print("2 - Adicionar música")
        print("3 - Remover música")
        print("4 - Excluir playlist")
        print("5 - Ver playlists")
        print("0 - Voltar")

        escolha = int(input("Escolha: "))
        if escolha == 1:
            nome = input("Nome da nova playlist: ")
            playlists.setdefault(usuario_logado, {})[nome] = []
            print("Playlist criada!")
        elif escolha == 2:
            nome = input("Nome da playlist: ")
            musica = input("Música para adicionar: ")
            if nome in playlists.get(usuario_logado, {}):
                playlists[usuario_logado][nome].append(musica)
                print("Música adicionada!")
            else:
                print("Playlist não existe.")
        elif escolha == 3:
            nome = input("Nome da playlist: ")
            musica = input("Música para remover: ")
            if musica in playlists.get(usuario_logado, {}).get(nome, []):
                playlists[usuario_logado][nome].remove(musica)
                print("Música removida.")
            else:
                print("Música não encontrada.")
        elif escolha == 4:
            nome = input("Nome da playlist a excluir: ")
            if nome in playlists.get(usuario_logado, {}):
                del playlists[usuario_logado][nome]
                print("Playlist excluída.")
            else:
                print("Playlist não encontrada.")
        elif escolha == 5:
            print("Suas playlists:")
            for nome, musicas in playlists.get(usuario_logado, {}).items():
                print(f"{nome}: {musicas}")
        elif escolha == 0:
            break
        else:
            print("Opção inválida.")