import pymongo
import pymongo.errors

def inserirgeral():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        db = client["InstaBooks"]
        livro_collection = db["Livros"]
        user_collection = db["Usuários"]
        inter_collection = db["Interações"]

        opca = input("Olá, o que você deseja inserir (usuário,livro,curtida ou comentário)? ")

        if opca == "usuário":
            aba1 = input("Insira o seu nome: ")
            aba2 = input("Insira o seu email: ")
            usuario = {
            "Nome": aba1,
            "Email": aba2,
            "LivrosLidos": [],
            "LivrosFavoritos": [],
            "Seguidores": [],
            "Seguindo": []
            }
            user_collection.insert_one(usuario)
            print("Perfil criado com sucesso!")
        elif opca == "livro":
            aba1 = input("Insira o título do livro: ")
            aba2 = input("Qual o autor do livro? ")
            aba3 = input("Qual o gênero do livro? ")
            aba4 = input("Qual a editora do livro? ")
            nota = [
                float(input("Avaliações do livro: "))]
            
            post = {"Título": aba1, "Autor": aba2, "Gênero": aba3, "Editora": aba4, "Avaliações": nota}
            livro_collection.insert_one(post)
            print("Livro inserido com sucesso!") 
        elif opca == "comentário":
            comentario = input("Digite o comentário: ")
            usuario_nome = input("Qual o autor que publicou o post do livro? ")
            livro_nome = input("Qual o nome do livro que deseja interagir? ")
            data = input("Data: ")
            # ... (lógica para inserir a interação)
            inter_collection.insert_one({"Tipo": opca, "Comentário": comentario, "Autor": usuario_nome, "Livro": livro_nome, "Data": data})
            print("Interação feita com sucesso!")
        elif opca == "curtida":
            usuario_nome = input("Qual o autor que publicou o post do livro? ")
            livro_nome = input("Qual o nome do livro que deseja interagir? ")
            nota = float(input("Digite a nota que você quer dar: "))
            data = input("Data: ")
            # ... (lógica para inserir a interação)
            inter_collection.insert_one({"Tipo": opca,"Nota": nota,"Autor": usuario_nome, "Livro": livro_nome, "Data": data})
            print("Interação feita com sucesso!")
        else:
            print("Opção inválida.")
        continuar = input("Deseja fazer outra atualização? (sim/não): ")
        if continuar.lower() != "sim":
            break