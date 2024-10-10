import pymongo
import pymongo.errors

def attuser():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        collection = db["Interações"]

        tipo_atualizacao = input("O que você deseja atualizar? (usuário, livro, interação): ")

        if tipo_atualizacao == "usuário":
            nameuser = input("Digite o nome do usuário: ")
            novo_livro = input("Digite o título do livro lido: ")
            # ... (lógica para adicionar o livro à lista de livros lidos)
            collection.update_one({"Nome": nameuser,"LivrosLidos": {"livro": novo_livro}})
            print("\nAtualização feita com sucesso!")

        elif tipo_atualizacao == "livro":
            livro_nome = input("Digite o nome do livro: ")
            nova_avaliacao = input("Digite a nova avaliação: ")
            # ... (lógica para adicionar a nova avaliação à lista de avaliações)
            collection.update_one({"Nome": livro_nome, "Avaliações": {"Avaliação": nova_avaliacao}})
            print("\nAtualização feita com sucesso!")

        elif tipo_atualizacao == "interação":
            interacao_id = input("Digite o ID da interação(nome): ")
            novo_comentario = input("Digite o novo comentário: ")
            # ... (lógica para atualizar o comentário da interação)
            collection.update_one({"Usuário": interacao_id, "Comentário": novo_comentario})
            print("\nAtualização feita com sucesso!")

        else:
            print("Opção inválida.")
attuser()