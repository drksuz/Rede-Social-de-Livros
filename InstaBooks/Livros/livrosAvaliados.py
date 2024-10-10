import pymongo
import pymongo.errors

def livros_mais_avaliados():
    # Conectando ao banco
    client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
    # Acessando o banco
    db = client["InstaBooks"]
    collection = db["Livros"]

    pipeline = [
        {"$unwind": "$Avaliações"},
        {"$group": {"_id": "$Título", "total_avaliacoes": {"$sum": 1}}},
        {"$sort": {"total_avaliacoes": -1}}
    ]
    result = db.livros.aggregate(pipeline)
    return list(result)
livros_mais_avaliados()