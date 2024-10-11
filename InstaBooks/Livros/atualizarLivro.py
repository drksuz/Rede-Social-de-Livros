import pymongo
import pymongo.errors

def atualizar_livro():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        collection = db["Livros"]

        livro_nome = input("Digite o nome do livro: ")
        nova_avaliacao = float(input("Digite a nova avaliação: "))

        collection.update_one({"Nome": livro_nome}, {"$push": {"Avaliações": nova_avaliacao}})
        print("Avaliação adicionada ao livro com sucesso!")

        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break
atualizar_livro()