import lib, os, time 
def main():
    inciar = lib.menu_principal('projeto_final.py/matriculas.csv')
    time.sleep(2)
    os.system('cls')
    while inciar:
        print("\nO que deseja fazer?")
        print("1. Listar livros")
        print("2. Adicionar livro")
        print("3. Buscar por titulo")
        print("4. buscar por genero")
        print("5. buscar por autor")
        print("6. Ver livros disponiveis para retirar")
        print("7. retirar livro")
        print("8. Sair")

                    
        escolha = input("Escolha uma opção: ")
                    
        if escolha == '1':
            lib.listar_livros('projeto_final.py/livros.csv')
        elif escolha == '2':
            titulo = input("Título: ")
            lib.adicionar_livro('projeto_final.py/livros.csv', titulo)
            print("Livro adicionado com sucesso!")
        elif escolha == '3':
            titulo = input("Título do livro que deseja buscar: ")
            livro = lib.buscar_livro('projeto_final.py/livros.csv', titulo)
            if livro:
                print(f"Livro encontrado: Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]}")
            else:
                print("Livro não encontrado!")
        elif escolha == '4':
            genero = input("Gênero do livro que deseja buscar: ")
            livros = lib.buscar_por_genero('projeto_final.py/livros.csv', genero)
            if livros:
                print("Livros encontrados:")
                for livro in livros:
                    print(f"Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]}")
            else:
                print("Nenhum livro encontrado para esse gênero!")
        elif escolha == '5':
            autor = input("Autor do livro que deseja buscar: ")
            livros = lib.buscar_por_autor('projeto_final.py/livros.csv', autor)
            if livros:
                print("Livros encontrados:")
                for livro in livros:
                    print(f"Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]}")
            else:
                print("Nenhum livro encontrado para esse autor!")
        elif escolha == '6':
            livros = lib.livros_disponiveis('projeto_final.py/livros.csv')
            if livros:
                print("Livros disponíveis para retirar:")
                for livro in livros:
                    print(f"Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]} | Quantidade: {livro[4]}")
            else:
                print("Nenhum livro disponível para retirar!")
        elif escolha == '7':
            titulo = input("Título do livro que deseja buscar para pegar retirar: ")
            quantidade = int(input("Quantidade de deste livro que deseja retirar "))
            
            livro = lib.retirar_livro('projeto_final.py/livros.csv', titulo, quantidade)
            if livro:
                print(f"Livro: Título: {livro[0]} | Autor: {livro[1]} | Gênero: {livro[2]} | Status: {livro[3]} | Quantidade: {livro[4]}")
                print("livro retirado com sucesso!")
        
        elif escolha == '8':
            print("Saindo...")  
            break
        else:
            print("Opção inválida! Tente novamente.")



if __name__ == "__main__":
    main()

