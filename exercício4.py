# Exercício 04
# Crie uma agenda de telefones que salva os dados de maneira
# permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome,
# telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1- Novo contato (create)
# ▶ 2- Procura (pelo nome) (read)
# ▶ 3- Atualiza contato (update)
# ▶ 4- Apaga contato (delete)
# ▶ 0- Sair

# O programa deve ser capaz de criar, ler, atualizar e apagar contatos

# Define o menu de opções como um dicionário
menu = {
    1: "Novo contato",
    2: "Procurar contato",
    3: "Atualizar contato",
    4: "Apagar contato",
    0: "Sair"
}

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = exibir_menu() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Novo contato
            novo_contato() # Chama a função novo_contato
        elif escolha == 2: # Procurar contato
            procurar_contato() # Chama a função procurar_contato
        elif escolha == 3: # Atualizar contato
            atualizar_contato() # Chama a função atualizar_contato
        elif escolha == 4: # Apagar contato
            apagar_contato() # Chama a função apagar_contato
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida
    

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

def novo_contato():
    """
    Função para adicionar um novo contato à agenda.
    """
    print("Novo contato:")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    # Abre o arquivo contatos.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_contatos = open("contatos.txt", "a")
    # Grava o contato no arquivo
    arquivo_contatos.write(f"{nome},{sobrenome},{telefone},{email}\n") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_contatos.close()
    print("Contato adicionado com sucesso!") # Mensagem de sucesso
    
def procurar_contato():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    print("Procurar contato:")
    nome_procurar = input("Digite o nome do contato que deseja procurar: ")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("contatos.txt", "r") as arquivo_contatos:
        conteudo = arquivo_contatos.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome, sobrenome, telefone, email = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_procurar.lower() == nome.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Nome: {nome}, Sobrenome: {sobrenome}, Telefone: {telefone}, E-mail: {email}")
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Contato não encontrado.") # Mensagem de erro se o contato não for encontrado
        
def atualizar_contato():
    """
    Atualiza os dados de um contato existente na agenda.
    :return: None
    """
    print("Atualizar contato:")
    nome_atualizar = input("Digite o nome do contato que deseja atualizar: ")
    # Abre o arquivo contatos.txt para leitura
    arquivo_contatos = open("contatos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_contatos.readlines()
    # Fecha o arquivo
    arquivo_contatos.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        nome, sobrenome, telefone, email = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_atualizar.lower() == nome.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Contato encontrado: {linha.strip()}") # Imprime os dados do contato encontrado
            # Atualiza os dados do contato
            novo_nome = input("Digite o novo nome (deixe em branco para não alterar): ")
            novo_sobrenome = input("Digite o novo sobrenome (deixe em branco para não alterar): ")
            novo_telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
            novo_email = input("Digite o novo e-mail (deixe em branco para não alterar): ")
            # Atualiza os dados do contato, se o usuário não deixar o nome em branco
            if novo_nome:
                conteudo[i] = f"{novo_nome},{novo_sobrenome},{novo_telefone},{novo_email}\n"
            else:
                conteudo[i] = f"{nome},{sobrenome},{telefone},{email}\n"
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Contato não encontrado.") # Mensagem de erro se o contato não for encontrado
        
    # Abre o arquivo contatos.txt para escrita
    arquivo_contatos = open("contatos.txt", "w")
    # Grava os contatos atualizados no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_contatos.write(linha) # Grava a linha no arquivo contatos.txt
    # Fecha o arquivo
    arquivo_contatos.close()
    print("Contato atualizado com sucesso!") # Mensagem de sucesso
    
def apagar_contato():
    """
    Apaga um contato da agenda.
    :return: None
    """
    nome_apagar = input("Digite o nome do contato que deseja apagar: ")
    # Abre o arquivo contatos.txt para leitura
    arquivo_contatos = open("contatos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_contatos.readlines()
    # Fecha o arquivo
    arquivo_contatos.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo):
        nome, sobrenome, telefone, email = linha.strip().split(",")
        if nome_apagar.lower() == nome.lower():
            print(f"Contato encontrado: {linha.strip()}")
            # Remove o contato da lista
            conteudo.pop(i)
            break
    else: # Se não encontrar o contato
        print("Contato não encontrado.")
        
    # Abre o arquivo contatos.txt para escrita
    arquivo_contatos = open("contatos.txt", "w")
    # Grava os contatos restantes no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_contatos.write(linha) # Grava a linha no arquivo contatos.txt
    # Fecha o arquivo
    arquivo_contatos.close()
    print("Contato apagado com sucesso!") # Mensagem de sucesso
    
def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() # Encerra o programa
            
if __name__ == "__main__":
    main() # Chama a função main para iniciar o programa