import pymongo

def interacoes():
    try: 
        # Conectando ao banco
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco
        db = client["InstaBooks"]
        collection = db["Interações"]

        tipo_interacao = input("Qual tipo de interação deseja fazer (curtida ou comentário)? ")

        # lógica para se o tipo de interação for igual a...
        if tipo_interacao == "comentário":
            comentario = input("Digite o comentário: ")
            usuario_nome = input("Qual o usuário que publicou o post do livro? ")
            livro_nome = input("Qual o nome do livro que deseja interagir? ")
            data = input("Data: ")
            # ... (lógica para inserir a interação)
            collection.insert_one({"Tipo": tipo_interacao,"Usuário": usuario_nome, "Comentário": comentario, "Livro": livro_nome, "Data": data})
            print("\nInteração feita com sucesso!")

        elif tipo_interacao == "curtida":
            usuario_nome = input("Qual o usuário que publicou o post do livro? ")
            livro_nome = input("Qual o nome do livro que deseja interagir? ")
            data = input("Data: ")
            # ... (lógica para inserir a interação)
            collection.insert_one({"Tipo": tipo_interacao,"Usuário": usuario_nome, "Livro": livro_nome, "Data": data})
            print("\nInteração feita com sucesso!")
        else:
            print("Interação não concluida.")
    except pymongo.errors as e:
        print("Erro ao interagir.", e)
interacoes()