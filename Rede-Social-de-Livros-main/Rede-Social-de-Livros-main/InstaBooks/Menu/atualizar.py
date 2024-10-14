import pymongo
import pymongo.errors

def atualizargeral():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        livro_collection = db["Livros"]
        user_collection = db["Usuários"]
        inter_collection = db["Interações"]

        tipo_atualizacao = input("Olá, o que você deseja atualizar (usuário,livro,curtida ou comentário)? ")

        if tipo_atualizacao == "usuário":
            nameuser = input("Digite o nome do usuário: ")
            novo_livro = input("Digite o título do livro lido e a data que leu: ")
            livro_favorito = input("Digite o título do seu livro favorito: ")
            user_collection.update_one(
            {"Nome": nameuser},
            {"$addToSet": {"LivrosLidos": novo_livro}}
            )
            user_collection.update_one(
            {"Nome": nameuser},
            {"$addToSet": {"LivrosFavoritos": livro_favorito}}
            )
            print("Livro adicionado à lista de livros lidos do usuário com sucesso!")
        elif tipo_atualizacao == "livro":
            nomelivro = input("Digite o título do livro que deseja avaliar: ")
            nota = float(input("Digite a nota que deseja avaliar para o livro: "))
            livro_collection.update_one(
            {"Título": nomelivro},
            {"$addToSet": {"Avaliações": nota}}
            )
            print("Avaliação feita com sucesso!")
        elif tipo_atualizacao == "comentário":
            interacao_id = input("Digite o Autor do livro: ")
            novo_comentario = input("Digite o novo comentário: ")
            inter_collection.update_one({"Autor": interacao_id}, {"$set": {"Comentário": novo_comentario}})
            print("Comentário atualizado com sucesso!")
        elif tipo_atualizacao == "curtida":
            interacao_id = input("Digite o Autor do livro: ")
            nova_nota = float(input("Digite a nova nota: "))
            inter_collection.update_one({"Autor": interacao_id}, {"$set": {"Nota": nova_nota}})
            print("Nota atualizada com sucesso!")
        else:
            print("Opção inválida.")
        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break