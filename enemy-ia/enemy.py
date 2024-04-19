from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# As entradas para as informações do inimigo seguem a seguinte ordem:
# Col 1 = Armado
# Col 2 = Armadura
# Col 3 = Resiste Magia
# Col 4 = Inimigo Grande
enemyEntry = [
    [0, 0, 0, 0],  # 1
    [1, 0, 0, 0],  # 1
    [0, 0, 0, 1],  # 1
    [0, 0, 1, 0],  # 1
    [0, 1, 0, 0],  # 2
    [1, 1, 0, 0],  # 2
    [1, 0, 1, 0],  # 3
    [0, 1, 1, 0],  # 3
    [0, 1, 0, 1],  # 3
    [0, 0, 1, 1],  # 3
    [1, 0, 0, 1],  # 4
    [1, 1, 1, 0],  # 4
    [1, 1, 0, 1],  # 5
    [1, 0, 1, 1],  # 5
    [0, 1, 1, 1],  # 6
    [1, 1, 1, 1]  # 7
]

# Resultado de acordo com as propriedades informadas do inimigo
# 1 = Muito Fraco
# 7 = Muito Forte
enemyStrength = [
    1,
    1,
    1,
    1,
    2,
    2,
    3,
    3,
    3,
    3,
    4,
    4,
    5,
    5,
    6,
    7
]

# Definição da rede neural
enemyAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(150, 150), random_state=1)
# Treina a rede neural para encaixar os dois arrays
enemyAI.fit(enemyEntry, enemyStrength)
print("Rede Neural Treinada!")

# Lista de string com questões para iterar abaixo
questions = [
    "está armado?",
    "está vestindo armadura?",
    "tem resistencia mágica?",
    "é grande?",
]

# Array com os valores inseridos
searchQuery = []
# Posição de index de qual pergunta é a atual
questionPosition = 0
# O tamanho do array de pesquisa precisa ser 4 (mesma quantidade de colunas da matriz enemyEntry
while len(searchQuery) < 4:
    # define a variável option primeiro, para evitar que qualquer valor além de 1 ou 0 seja inserido
    option = -1
    while option != 0 and option != 1:
      option = int(input(f"O inimigo {questions[questionPosition]} (Responder somente com 0 ou 1. 0=Não, 1=Sim)\n"))

    # Adiciona o valor digitado de option para o array de search query
    searchQuery.append(option)
    # Muda a posição do index de pergunta para a próxima da lista
    questionPosition += 1

# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1], Resposta: [7]
result = enemyAI.predict([searchQuery])
print(result)

