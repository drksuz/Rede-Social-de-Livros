import pymongo
import pymongo.errors

def usuariomenu():
    while True:
        # Conectando no banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")

        # Acessando o banco de dados e a coleção
        
        db = client["InstaBooks"]
        collection = db["Usuários"]
