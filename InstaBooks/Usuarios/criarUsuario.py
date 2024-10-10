import pymongo

def inserindoUsuario():
    try: 
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Usuários"]

        aba1 = input("Insira o seu nome completo: ")
        aba2 = input("Insira o seu email: ")
        aba3 = input("Quais livros você já leu: ")
        aba4 = input("Quais seus livros favoritos: ")

        post = {"Nome": aba1, "Email": aba2, "LivrosLidos": aba3, "LivrosFavoritos": aba4}

        post_id = collection.insert_one(post)

        print("Perfil criado com sucesso!")
    except pymongo.errors as e:
        print("Erro ao inserir dados", e)
inserindoUsuario()