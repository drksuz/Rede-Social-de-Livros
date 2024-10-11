import pymongo

def livro():
    try: 
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Livros"]

        aba1 = input("Insira o título do livro: ")
        aba2 = input("Qual o autor do livro? ")
        aba3 = input("Qual o gênero do livro? ")
        aba4 = input("Qual a editora do livro? ")
        nota = [
            float(input("Avaliações do livro: "))]

        post = {"Título": aba1, "Autor": aba2, "Gênero": aba3, "Editora": aba4, "Avaliações": nota}

        
        post_id = collection.insert_one(post)

        print("Livro inserido com sucesso!") 
    except pymongo.errors as e:
        print("Erro ao inserir dados", e)
livro()