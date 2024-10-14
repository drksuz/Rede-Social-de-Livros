import pymongo

def ccategoria():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Usuários"]

        # Perguntando ao usuário quem ele quer consultar
        name = input("Qual o nome do usuário que você deseja consultar? ")

        # Encontrando o usuário
        results = collection.find({"Nome": name})

        for product in results:
            print(product)
        continuar = input("\nDeseja fazer outra consulta? (sim/não): ")
        if continuar.lower() != "sim":
            break