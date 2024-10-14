import pymongo

def excluirlivro():
    while True:
        """Exclui um Livro com o nome especificado."""

        # Conectar ao banco de dados
        client = pymongo.MongoClient("mongodb+srv://daricksouza:darick123@cluster0.gtemi.mongodb.net/")
        db = client["InstaBooks"]
        collection = db["Livros"]

        # Pedindo o nome do livro para deletar
        nomeexcluir = input("Digite o título do livro que deseja remover: ")

        # Definir o filtro para encontrar o livro com o nome exato
        filtro = {"Título": nomeexcluir}

        # Excluir o livro que corresponde ao filtro
        result = collection.delete_one(filtro)

        if result.deleted_count == 1:
            print(f"Livro '{nomeexcluir}' excluído com sucesso.")
        else:
            print(f"Nenhum livro com o nome '{nomeexcluir}' encontrado.")
        continuar = input("Deseja excluir outro livro? (sim/não): ")
        if continuar.lower() != "sim":
            break