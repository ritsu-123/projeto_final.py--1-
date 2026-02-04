import csv
def salvar_csv(arquivo, livros):
    """
    Recebe uma matriz e sobrescreve o arquivo CSV com os dados.
    """
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

            print(f"{i + 1}. Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]} | ") 


def adicionar_livro(arquivo, titulo, autor, genero):
    livros = ler_livros(arquivo)
    novo_livro = [titulo, autor, genero, "disponivel"]
    livros.append(novo_livro)
    salvar_csv(arquivo, livros)

def cadrastar_usuario(arquivo, matricula, senha):
    usuarios = ler_livros(arquivo)
    novo_usuario = [matricula, senha]
    usuarios.append(novo_usuario)
    salvar_csv(arquivo, usuarios)
    print(f"Usuário {matricula} cadastrado com sucesso!")

def ler_usuarios(arquivo):
    usuarios = ler_livros(arquivo)
    return usuarios

def entrar_conta(arquivo, matricula, senha):
    usuarios = ler_usuarios(arquivo)
    for usuario in usuarios:
        if usuario[0] == matricula and usuario[1] == senha:
            return True
    return False

def buscar_livro(arquivo, titulo):
    livros = ler_livros(arquivo)
    chave = titulo.strip().lower()
    for livro in livros:
        if chave in livro[0].lower():
            return livro
    return None

def emprestar_livro(arquivo, titulo):
    livros = ler_livros(arquivo)
    chave = titulo.strip().lower()
    for livro in livros:
        if chave in livro[0].lower():
            if int(livro[4]) == 1:
                livro[3] = "emprestado"
                livro[4] = "0"
                salvar_csv(arquivo, livros)
                return livro
            elif int(livro[4]) > 1:
                livro[4] = str(int(livro[4]) - 1)
                salvar_csv(arquivo, livros)
                return livro
            elif livro[4] == "0":
                print("Não temos mais cópias deste livro!")
            
def devolvar_livro(arquivo, titulo):
    livros = ler_livros(arquivo)
    chave = titulo.strip().lower()
    for livro in livros:
        if chave == livros[0]:
            if livro[3] == "emprestado":
                livro[3] == "disponivel"
                salvar_csv(arquivo, livro)
                return True
            else:
                return False

                