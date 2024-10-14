import pymongo

def consultargeral():
    while True:
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        userr_collection = db["Usuários"]
        book_collection = db["Livros"]
        intera_collection = db["Interações"]

        # Perguntando ao usuário quem ele quer consultar
        op = input("O que você deseja consultar (usuário,livro ou interação?) ")

        if op == "usuário":
            # Perguntando ao usuário quem ele quer consultar
            name = input("Qual o nome do usuário que você deseja consultar? ")
            # Encontrando o usuário
            results = userr_collection.find({"Nome": name})
            for product in results:
                print(product)
            else:
                print("Usuário não encontrado.")
        elif op == "livro":
            # Perguntando ao usuário qual livro ele quer consultar
            name = input("Qual o título do livro que você deseja consultar? ")
            # Encontrando o usuário
            results = book_collection.find({"Título": name})
            for product in results:
                print(product)
            else:
                print("Livro não encontrado.")
        elif op == "interação":
            # Perguntando ao usuário qual interação ele quer consultar
            name = input("Qual o autor você deseja consultar? ")

            # Encontrando o usuário
            results = intera_collection.find({"Autor": name})

            for product in results:
                print(product)
        else:
            print("Interação não encontrada.")
        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break