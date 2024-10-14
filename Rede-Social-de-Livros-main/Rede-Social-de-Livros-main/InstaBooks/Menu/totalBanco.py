import pymongo
import pymongo.errors

def totalbd():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]

        print("Olá, você está na parte de totalização do banco, veja as opções:")
        print("1. Visualizar total de usuários.")
        print("2. Visualizar total de livros.")
        print("3. Visualizar total de interações.")

        opcao = input("Qual a opção você escolheu? ")

        if opcao == '1':
            collection = db["Usuários"]
            total_usuarios = collection.count_documents({})
            print(f"O total de usuários na rede social é de: {total_usuarios}")
        elif opcao == '2':
            collection = db["Livros"]
            total_livros = collection.count_documents({})
            print(f"O total de livros na rede social é de: {total_livros}")
        elif opcao == '3':
            collection = db["Interações"]
            total_interacoes = collection.count_documents({})
            print(f"O total de interações na rede social é de: {total_interacoes}")    
        else:
            print("Opção inválida.")
        continuar = input("Deseja fazer outro cálculo? (sim/não): ")
        if continuar.lower() != "sim":
            break