import pymongo
import pymongo.errors

def interacao():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Interações"]

        print("\n----------Seja bem vindo à InstaBooks----------")
        print("1. Criar um novo perfil.")
        print("2. Adicionar livros à sua lista de leitura.")
        print("3. Avaliar livros.")
        print("4. Seguir outros usuários.")
        print("5. Visualizar Top 5 livros mais avaliados.")
        print("6. Identificar os autores mais seguidos.")
        print("7. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            ()
        elif opcao == '2':
            ()
        elif opcao == '3':
            ()
        elif opcao == '4':
            ()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")