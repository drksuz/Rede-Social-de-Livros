import pymongo
import pymongo.errors

def deletargeral():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        livro_collection = db["Livros"]
        user_collection = db["Usuários"]
        inter_collection = db["Interações"]

        tipo_atualizacao = input("Olá, o que você deseja deletar (usuário,livro ou interação)? ")

        if tipo_atualizacao == "usuário":
            nomeexcluir = input("Digite o nome da conta do usuário que deseja remover: ")
            # Definir o filtro para encontrar o usuário com o nome exato
            filtro = {"Nome": nomeexcluir}
            # Excluir o usuário que corresponde ao filtro
            user_collection.delete_one(filtro)
            print("Usuário removido com sucesso!")
        elif tipo_atualizacao == "livro":
            # Pedindo o nome do livro para deletar
            nomeexcluir = input("Digite o título do livro que deseja remover: ")
            # Definir o filtro para encontrar o livro com o nome exato
            filtro = {"Título": nomeexcluir}
            # Excluir o livro que corresponde ao filtro
            livro_collection.delete_one(filtro)
            print("Livro removido com sucesso!")
        elif tipo_atualizacao == "interação":
            # Pedindo o nome do autor para deletar
            nomeexcluir = input("Digite o Autor para remover a interação: ")
            # Definir o filtro para encontrar o autor com o nome exato
            filtro = {"Autor": nomeexcluir}
            # Excluir a interação que corresponde ao filtro
            inter_collection.delete_one(filtro)
        else:
            print("Opção inválida.")
        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break