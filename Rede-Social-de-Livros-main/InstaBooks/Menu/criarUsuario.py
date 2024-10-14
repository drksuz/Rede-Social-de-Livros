import pymongo

def inserindoUsuario():
    try: 
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Usuários"]

        aba1 = input("Insira o seu nome: ")
        aba2 = input("Insira o seu email: ")

        usuario = {
            "Nome": aba1,
            "Email": aba2,
            "LivrosLidos": [],
            "LivrosFavoritos": [],
            "Seguidores": [],
            "Seguindo": []
        }

        #"LivrosLidos": aba3, "LivrosFavoritos": aba4

        post_id = collection.insert_one(usuario)

        print("Perfil criado com sucesso!")
    except pymongo.errors as e:
        print("Erro ao inserir dados", e)