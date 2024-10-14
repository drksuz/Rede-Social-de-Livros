import pymongo
import pymongo.errors

def livros_mais_avaliados():
    while True:

        # Conectando ao banco de dados MongoDB
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]
        collection = db["Livros"]

        # Buscar os 5 livros mais bem avaliados (ordenando pelo campo 'rating' em ordem decrescente)
        top_livros = collection.find().sort("rating", -1).limit(5)

        print("\nTop 5 Livros Mais Bem Avaliados:")
        for i, livro in enumerate(top_livros, 1):
            print(f"{i}. {livro['Título']} - Avaliação: {livro['Avaliações']}")
        break