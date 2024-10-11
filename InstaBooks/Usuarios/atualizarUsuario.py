import pymongo
import pymongo.errors

def attuser():
    
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        collection = db["Usuários"]

        nameuser = input("Digite o nome do usuário: ")
        novo_livro = input("Digite o título do livro lido: ")
        livro_favorito = input("Digite o título do seu livro favorito: ")
        collection.update_one({"Nome": nameuser}, {"$push": {"LivrosLidos": novo_livro}, "$push": {"LivrosFavoritos": livro_favorito}})
        print("Livro adicionado à lista de livros lidos do usuário com sucesso!")

        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break
attuser()