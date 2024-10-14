import pymongo
import pymongo.errors

def avaliar_livro():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        collection = db["Livros"]

        nomelivro = input("Digite o título do livro que deseja avaliar: ")
        nota = float(input("Digite a nota que deseja avaliar para o livro: "))

        collection.update_one(
        {"Título": nomelivro},
        {"$addToSet": {"Avaliações": nota}}
        )
        print("Avaliação feita com sucesso!")
        continuar = input("Deseja fazer outra interação? (sim/não): ")
        if continuar.lower() != "sim":
            break