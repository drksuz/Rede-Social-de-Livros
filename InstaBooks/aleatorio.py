import json
import random

def gerar_usuario():
    """Gera um usuário aleatório com nome e email."""
    nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Luiza", "Rafael", "Beatriz", "André", "Juliana"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Rodrigues", "Costa", "Almeida", "Fernandes", "Lima"]
    emails = ["@gmail.com", "@hotmail.com", "@outlook.com"]

    nome = random.choice(nomes) + " " + random.choice(sobrenomes)
    email = nome.lower().replace(" ", ".") + random.choice(emails)

    return {"nome": nome, "email": email}

# Gera uma lista de 50 usuários
usuarios = [gerar_usuario() for _ in range(50)]

# Salva a lista de usuários em um arquivo JSON
with open("usuarios.json", "w") as arquivo:
    json.dump(usuarios, arquivo, indent=4)
print("Arquivo 'usuarios.json' criado com sucesso!")
gerar_usuario()