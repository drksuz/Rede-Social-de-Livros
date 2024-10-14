import pymongo

def ccintera():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Interações"]

        # Perguntando ao usuário qual interação ele quer consultar
        name = input("Qual o autor você deseja consultar? ")

        # Encontrando o usuário
        results = collection.find({"Autor": name})

        for product in results:
            print(product)
        continuar = input("\nDeseja fazer outra consulta? (sim/não): ")
        if continuar.lower() != "sim":
            break