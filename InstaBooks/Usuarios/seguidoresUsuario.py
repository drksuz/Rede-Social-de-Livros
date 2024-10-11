import pymongo

def seguir_usuario():
    client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
    db = client["InstaBooks"]
    collection = db["Usuários"]
    
    usuario_seguir = input("Digite o nome do usuário que deseja seguir: ")
    seu_usuario = input("Digite o seu nome de usuário: ")

    # Aqui você precisará buscar o ID do usuário a partir do nome
    # ... (código para buscar o ID)

    collection.update_one(
        {"Nome": seu_usuario},
        {"$addToSet": {"Seguindo": usuario_seguir}}
    )
    collection.update_one(
        {"Nome": usuario_seguir},
        {"$addToSet": {"Seguidores": seu_usuario}}
    )
    print(f"Você agora está seguindo {usuario_seguir}!")
def deixar_seguir():
    
seguir_usuario()