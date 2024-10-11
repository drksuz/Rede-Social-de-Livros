import pymongo

def excluirproduto():
    """Exclui um usuário com o nome especificado."""

    # Conectar ao banco de dados
    client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
    db = client["InstaBooks"]
    collection = db["Usuários"]

    # Pedindo o nome do usuário para deletar
    nomeexcluir = input("Digite o nome da conta do usuário que deseja remover: ")

    # Definir o filtro para encontrar o usuário com o nome exato
    filtro = {"Nome": nomeexcluir}

    # Excluir o usuário que corresponde ao filtro
    result = collection.delete_one(filtro)

    if result.deleted_count == 1:
        print(f"Usuário '{nomeexcluir}' excluído com sucesso.")
    else:
        print(f"Nenhum usuário com o nome '{nomeexcluir}' encontrado.")
excluirproduto()