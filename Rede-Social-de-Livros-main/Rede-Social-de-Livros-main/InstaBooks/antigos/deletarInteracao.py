import pymongo

def excluirinteracao():
    while True:    
        """Exclui uma interação com o autor especificado."""

        # Conectar ao banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]
        collection = db["Interações"]

        # Pedindo o nome do autor para deletar
        nomeexcluir = input("Digite o Autor para remover a interação: ")

        # Definir o filtro para encontrar o autor com o nome exato
        filtro = {"Autor": nomeexcluir}

        # Excluir a interação que corresponde ao filtro
        result = collection.delete_one(filtro)

        if result.deleted_count == 1:
            print("Interação excluída com sucesso.")
        else:
            print(f"Nenhum interação encontrada.")
        continuar = input("Deseja excluir outra interação? (sim/não): ")
        if continuar.lower() != "sim":
            break