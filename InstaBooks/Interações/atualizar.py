import pymongo
import pymongo.errors

def att():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        collection = db["Interações"]

        tipo_atualizacao = input("Que tipo de interação você deseja atualizar (curtida,comentário)? ")

        if tipo_atualizacao == "comentário":
            interacao_id = input("Digite o ID da interação(nome): ")
            novo_comentario = input("Digite o novo comentário: ")
            collection.update_one({"Usuário": interacao_id}, {"$set": {"Comentário": novo_comentario}})
            print("Comentário atualizado com sucesso!")
        elif tipo_atualizacao == "curtida":
            interacao_id = input("Digite o ID da interação(nome): ")
            novo_comentario = input("Digite o novo comentário: ")
            collection.update_one({"Usuário": interacao_id}, {"$set": {"Comentário": novo_comentario}})
            print("Comentário atualizado com sucesso!")
        else:
            print("Opção inválida.")
        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break
att()