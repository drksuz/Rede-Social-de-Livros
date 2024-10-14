import pymongo
import pymongo.errors

def usuarios_mais_avaliados():
    try:
        # Conectando ao banco de dados MongoDB
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]
        collection = db["Usuários"]

        # Buscar os 5 usuários mais seguidos, ordenando pelo campo 'seguidores' em ordem decrescente
        top_usuarios = collection.find().sort("seguidores", -1).limit(3)

        print("\nTop 3 Usuários Mais Seguidos:")
        for i, usuario in enumerate(top_usuarios, 1):
            nome = usuario['Nome']
            seguidores = usuario['Seguidores']
            print(f"{i}. {nome} - Seguidores: {seguidores}")
    except Exception as e:
        print("Ocorreu um erro ao buscar os usuários:", e)