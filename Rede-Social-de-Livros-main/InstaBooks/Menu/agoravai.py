from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

# Conectando ao MongoDB
client = MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
db = client["InstaBooks"]

# Coleções
usuarios_collection = db["Usuários"]
livros_collection = db["Livros"]
interacoes_collection = db["Interações"]

# Inicializando o Faker
fake = Faker()

# Função para gerar usuários fictícios
"""def gerar_usuarios(num_usuarios=50):
    usuarios = []
    for _ in range(num_usuarios):
        nome = fake.name()
        email = fake.email()
        livros_lidos = [fake.sentence(nb_words=3) for _ in range(random.randint(1, 20))]  # Gerar entre 1 a 10 livros
        livros_favoritos = random.sample(livros_lidos, min(5, len(livros_lidos)))  # Escolher até 5 livros favoritos
 
        usuarios.append({
            "Nome": nome,
            "Email": email,
            "LivrosLidos": livros_lidos,
            "LivrosFavoritos": livros_favoritos,
            "Seguidores": [],
            "Seguindo": []
        })
    usuarios_collection.insert_many(usuarios)
    print(f"Inseridos {num_usuarios} usuários fictícios.")
gerar_usuarios()"""
"""def atualizar_seguidores_e_seguindo():
    # Obter todos os usuários do banco para associar seguidores e seguindo
    todos_usuarios = list(usuarios_collection.find({}, {"Nome": 1}))  # Buscando apenas os nomes
    nomes_usuarios = [usuario['Nome'] for usuario in todos_usuarios]
    # Atualizar os seguidores e seguindo para cada usuário
    for usuario in todos_usuarios:
        # Seleciona aleatoriamente entre 0 e 20 pessoas que o usuário está seguindo
        seguindo = random.sample(nomes_usuarios, random.randint(0, min(20, len(nomes_usuarios))))
        # Seleciona aleatoriamente entre 0 e 20 pessoas que seguem o usuário
        seguidores = random.sample(nomes_usuarios, random.randint(0, min(20, len(nomes_usuarios))))
        # Atualiza o usuário no banco com os seguidores e seguindo
        usuarios_collection.update_one(
            {"Nome": usuario['Nome']},
            {"$set": {"Seguidores": seguidores, "Seguindo": seguindo}}
        )
        print(f"Atualizados os seguidores e seguindo para usuários.")
atualizar_seguidores_e_seguindo()"""

"""# Função para gerar livros fictícios
def gerar_livros(num_livros=30):
    livros = []
    generos = ['Ficção', 'Aventura', 'Romance', 'Ficção Científica', 'História', 'Fantasia']
    for _ in range(num_livros):
        titulo = fake.sentence(nb_words=4)
        autor = fake.name()
        genero = random.choice(generos)
        editora = fake.company()
        avaliacoes = [random.randint(1, 5) for _ in range(random.randint(1, 100))]  # Entre 1 e 100 avaliações

        livros.append({
            "Título": titulo,
            "Autor": autor,
            "Gênero": genero,
            "Editora": editora,
            "Avaliações": avaliacoes
        })
    livros_collection.insert_many(livros)
    print(f"Inseridos {num_livros} livros fictícios.")
gerar_livros()"""

"""# Função para gerar interações fictícias
def gerar_interacoes(num_interacoes=80):
    interacoes = []
    tipos_interacao = ['curtida', 'comentário']

    # Obter todos os usuários e livros para aleatoriedade
    todos_usuarios = list(db["Usuários"].find({}, {"Nome": 1}))
    todos_livros = list(db["Livros"].find({}, {"Título": 1}))

    for _ in range(num_interacoes):
        tipo = random.choice(tipos_interacao)
        # Selecionar um usuário e um livro aleatoriamente
        users = random.choice(todos_usuarios)['Nome']
        livro = random.choice(todos_livros)['Título']
        if tipo =='curtida':
            nota = random.randint(1, 10)  # Nota de 1 a 5
            interacoes.append({
            "Tipo": tipo,
            "Nota": nota,
            "Autor": users,
            "Livro": livro,
            "Data": fake.date()
        })
        else:
            comentario = fake.sentence()  # Gera um comentário aleatório
            interacoes.append({
            "Tipo": tipo,
            "Comentário": comentario,
            "Autor": users,
            "Livro": livro,
            "Data": fake.date()
        })
        # Inserir interações no banco de dados
        interacoes_collection.insert_many(interacoes)
        print(f"Inseridas {num_interacoes} interações fictícias.")
gerar_interacoes(80)"""