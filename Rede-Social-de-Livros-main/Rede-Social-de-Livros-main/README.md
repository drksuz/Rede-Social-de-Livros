Um banco de dados no MongoDB Atlas que modele uma rede social para amantes de livros, onde os usuários podem criar perfis, adicionar livros à sua lista de leitura, avaliar livros e seguir outros usuários, realizando as seguintes operações:

CRUD: Criação, leitura, atualização e deleção de documentos representando usuários, livros e interações.
Agregação: Cálculo de métricas como número total de usuários, livros mais avaliados, autores mais seguidos, etc.
Índices: Criação de índices para otimizar consultas e melhorar o desempenho.

Estrutura do Banco de Dados:

Coleção Usuários:
id: ObjectId
nome: string
email: string
livrosLidos: array de objetos (cada objeto com _id do livro, avaliação e data de leitura)
livrosFavoritos: array de objetos (_id do livro)
seguindo: array de objetos (_id dos usuários seguidos)
seguidores: array de objetos (_id dos seguidores)

Coleção Livros:
id: ObjectId
título: string
autor: string
gênero: string
editora: string
avaliações: array de objetos (cada objeto com _id do usuário, avaliação e comentário)

Coleção Interações:
id: ObjectId
tipo: string (curtida, comentário, etc.)
usuário: ObjectId (referência ao usuário)
livro: ObjectId (referência ao livro)
data: data

Tarefas:
Modelagem:
Criar as coleções no MongoDB Atlas com os esquemas definidos acima.
Popular o banco com dados fictícios (pelo menos 50 usuários, 30 livros e 80 interações).

Operações CRUD:
Criação: Adicionar novos usuários, livros e interações.
Leitura: Consultar informações específicas de um usuário, livro ou interação.
Atualização: Alterar dados de um usuário (ex: adicionar um livro lido), livro (ex: adicionar uma nova avaliação) ou interação (ex: editar um comentário).
Deleção: Remover um usuário, livro ou interação.

Agregação:
Calcular o número total de usuários, livros e interações.
Encontrar os 5 livros mais bem avaliados.
Identificar os autores mais seguidos.

Índices:
Criar índices compostos para otimizar consultas como:
(livro, avaliação) para encontrar rapidamente as melhores avaliações de um livro.
(usuário, seguindo) para descobrir quem um usuário está seguindo.
