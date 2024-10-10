import pymongo
import pymongo.errors
import Usuarios.inserindo as inserindo
import Usuarios.consultarUsuario as consultarUsuario
import Usuarios.consultarP as consultarP
import Interações.atualizarUsuario as atualizarUsuario
import Usuarios.deletarUsuario as deletarUsuario

def menu():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        
        db = client["MercadinhoSouza"]
        collection = db["Produtos"]
        
    
        print("1. Inserir produtos")
        print("2. Consultar produtos por categoria")
        print("3. Consultar produtos por preço")
        print("4. Atualizar informações do produto")
        print("5. Deletar produto")
        print("6. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            inserindo.inserindo()
        elif opcao == '2':
            consultarUsuario.ccategoria()
        elif opcao == '3':
            consultarP.cpreco()
        elif opcao == '4':
            atualizarUsuario.atualizarproduto()
        elif opcao == '5':
            deletarUsuario.excluirproduto()
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    #except pymongo.errors.ConnectionFailure as e:
    #print(f"Erro de conexão com o banco de dados: {e}")
menu()