import pymongo

def cclivro():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Livros"]

        # Perguntando ao usuário qual livro ele quer consultar
        name = input("Qual o título do livro que você deseja consultar? ")

        # Encontrando o usuário
        results = collection.find({"Título": name})

        for product in results:
            print(product)
        continuar = input("\nDeseja fazer outra consulta? (sim/não): ")
        if continuar.lower() != "sim":
            break