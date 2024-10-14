import pymongo
import pymongo.errors
import criarUsuario
import atualizarUsuario
import avaliarLivro
import seguidoresUsuario
import usuariosMaisSeguidos
import adicionarLivro
import inserirInteracoes
import consultarUsuario
import consultarLivro
import consultarInteracao 
import atualizarLivro
import atualizarInteracao
import totalBanco
import livrosMaisAvaliados
import deletarUsuario
import deletarLivro
import deletarInteracao

def menuprincipal():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]
        
        print("----------Seja bem vindo à InstaBooks----------")
        print("1. Criar um novo usuário.")
        print("2. Inserir um novo livro.")
        print("3. Inserir uma nova interação.")
        print("4. Consultar um usuário.")
        print("5. Consultar um livro.")
        print("6. Consultar uma interação.")
        print("7. Atualizar um usuário.")
        print("8. Atualizar um livro.")
        print("9. Atualizar uma interação.")
        print("10. Deletar um usuário.")
        print("11. Deletar um livro.")
        print("12. Deletar uma interação.")
        print("13. Visualizar o número de usuários, livros e interações na rede social.")
        print("14. Encontrar os 5 livros mais bem avaliados.")
        print("15. Identificar os usuários mais seguidos.")
        print("16. Avaliar livros.")
        print("17. Seguir outros usuários.")
        print("18. Visualizar Top 5 livros mais avaliados.")
        print("29. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == "1":
            criarUsuario.inserindoUsuario()
        elif opcao == "2":
            adicionarLivro.livro()
        elif opcao == "3":
            inserirInteracoes.interacoes()
        elif opcao == "4":
            consultarUsuario.ccategoria()
        elif opcao == "5":
            consultarLivro.cclivro()
        elif opcao == "6":
            consultarInteracao.ccintera()
        elif opcao == "7":
            atualizarUsuario.attuser()
        elif opcao == "8":
            atualizarLivro.atualizar_livro()
        elif opcao == "9":
            atualizarInteracao.att()
        elif opcao == "10":
            deletarUsuario.excluirusuario()
        elif opcao == "11":
            deletarLivro.excluirlivro()
        elif opcao == "12":
            deletarInteracao.excluirinteracao()
        elif opcao == "13":
            totalBanco.totalbd()
        elif opcao == "14":
            livrosMaisAvaliados.livros_mais_avaliados()
        elif opcao == "15":
            usuariosMaisSeguidos.usuarios_mais_avaliados()
        elif opcao == "16":
            avaliarLivro.avaliar_livro()
        elif opcao == "17":
            seguidoresUsuario.seguir_usuario()
        elif opcao == "18":
            livrosMaisAvaliados.livros_mais_avaliados()
        elif opcao == "19":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
menuprincipal()