import csv, os

def salvar_csv(arquivo, livros):
    
    try:
        with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(livros)
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def ler_livros(arquivo):
    matriz = []
    try:
        with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                if linha:  
                    matriz.append(linha)


    except FileNotFoundError:
        return []

    return matriz

def listar_livros(arquivo):
    livros = ler_livros(arquivo)
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(livros ):

            print(f"{i + 1}. Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]} | Quantidade: {livro[4]}") 


def adicionar_livro(arquivo, titulo, quantidade):
    livros = ler_livros(arquivo)
    titulo_v2 = titulo.lower().strip()
    for livro in livros:
        if livro[0].lower().strip() == titulo_v2:
            livro[4] = str(int(livro[4]) + quantidade)
            salvar_csv(arquivo, livros)
            return
    autor = input("Autor: ")
    genero = input("Gênero: ")
    novo_livro = [titulo, autor, genero, "disponivel", str(quantidade)]
    livros.append(novo_livro)
    salvar_csv(arquivo, livros)




def cadastrar_usuario(arquivo):
    while True:
        matricula = int(input("Digite sua matrícula: "))
        senha = int(input("Digite sua senha: "))
        
        usuarios = ler_livros(arquivo)
        existe = False

        for usuario in usuarios:
            if int(usuario[0]) == matricula:
                print("Já existe um usuário cadastrado com essa matrícula! Tente novamente.")
                existe = True
                break
        
        if existe:
            continue
        
        novo_usuario = [matricula, senha]
        usuarios.append(novo_usuario)
        salvar_csv(arquivo, usuarios)
        print(f"Usuário {matricula} cadastrado com sucesso!")
        return True

def ler_usuarios(arquivo):    
    usuarios = ler_livros(arquivo)
    return usuarios


def entrar_conta(arquivo, matricula, senha):
    usuarios = ler_livros(arquivo)
    for usuario in usuarios:
        if int(usuario[0]) == matricula and int(usuario[1]) == senha:
            return True
    return False

def buscar_livro(arquivo, titulo):
    livros = ler_livros(arquivo)
    chave = titulo.strip().lower()
    for livro in livros:
        if chave in livro[0].lower():
            return livro

def buscar_por_genero(arquivo, genero):
    livros = ler_livros(arquivo)
    genero2 = genero.strip().lower()
    resultados = []
    for livro in livros:
        if genero2 in livro[2].lower():
            resultados.append(livro)
    return resultados

def buscar_por_autor(arquivo, autor):
    livros = ler_livros(arquivo)
    autor2 = autor.strip().lower()
    resultados = []
    for livro in livros:
        if autor2 in livro[1].lower():
            resultados.append(livro)
    return resultados

def livros_disponiveis(arquivo):
    livros = ler_livros(arquivo)
    disponiveis = []
    for livro in livros:
        if livro[3] == "disponivel" and int(livro[4]) > 0:
            disponiveis.append(livro)
    return disponiveis
def retirar_livro(arquivo, titulo, quantidade):
    livros = ler_livros(arquivo)
    titulo_v2 = titulo.strip().lower()
    for livro in livros:
        if titulo_v2 in livro[0].lower():
            if livro[3] == "disponivel" and int(livro[4]) > 0:
                if int(livro[4]) < quantidade:
                    print(f"Não há {quantidade} cópias disponíveis. Há apenas {livro[4]} cópias.")
                    return None
                livro[4] = str(int(livro[4]) - quantidade)
                if int(livro[4]) == 0:
                    livro[3] = "indisponivel"
                salvar_csv(arquivo, livros)
                return livro
            else:
                print("Livro indisponível.")
                return None
            

            
def menu_principal(arquivo):
    while True:
        print("\n📖 BEM-VINDO À NOSSA LIVRARIA!")
        opcao = int(input(
            "Digite:\n"
            "1 - Fazer login\n"
            "2 - Cadastrar usuário\n"
            "Escolha: "
        ))

        if opcao == 1:
            while True:
                matricula = int(input("Digite sua matrícula (apenas numeros): "))
                senha = int(input("Digite sua senha (apenas numeros): "))

                if entrar_conta(arquivo, matricula, senha):
                    print("Login realizado com sucesso!")
                    return True
                else:
                    erro_login = input("Matrícula ou senha incorretos! Deseja tentar novamente? (s/n): ")
                    if erro_login.lower() == 'n':
                        print("Voltando ao menu principal...")
                        break
                    elif erro_login.lower() != 's':
                        print("Opção inválida! Voltando ao menu principal...")
                        break
                


        elif opcao == 2:
            cadastrar_usuario(arquivo)
            print("Voltando ao menu...")

        else:
            print("Opção inválida! Tente novamente.")
        


            


                



