from sklearn.neural_network import MLPClassifier
from PIL import Image
import matplotlib.pyplot as plt
import random

enemies = [
    {
        "image": "./assets/001.webp",
        "name": "Jack Frost",
        "chance": 10
    },
    {
        "image": "./assets/002.webp",
        "name": "Jack-o-Lantern",
        "chance": 10
    },
    {
        "image": "./assets/003.webp",
        "name": "Pixie",
        "chance": 10
    },
    {
        "image": "./assets/004.webp",
        "name": "Lucifer",
        "chance": 0.25
    },
    {
        "image": "./assets/005.webp",
        "name": "Vishnu",
        "chance": 2.5
    },
    {
        "image": "./assets/006.webp",
        "name": "Angel",
        "chance": 10
    },
    {
        "image": "./assets/007.webp",
        "name": "Daemon",
        "chance": 10
    },
    {
        "image": "./assets/008.webp",
        "name": "Slime",
        "chance": 10
    },
    {
        "image": "./assets/009.webp",
        "name": "Metatron",
        "chance": 1
    },
    {
        "image": "./assets/010.webp",
        "name": "Chimera",
        "chance": 8
    },
    {
        "image": "./assets/011.webp",
        "name": "Cerberus",
        "chance": 5
    },
    {
        "image": "./assets/012.webp",
        "name": "Hecatoncheires",
        "chance": 6
    },
    {
        "image": "./assets/013.webp",
        "name": "Mada",
        "chance": 7
    },
    {
        "image": "./assets/014.webp",
        "name": "Loki",
        "chance": 3
    },
    {
        "image": "./assets/015.webp",
        "name": "Thor",
        "chance": 4
    },
    {
        "image": "./assets/016.webp",
        "name": "Shiva",
        "chance": 0.9
    },
    {
        "image": "./assets/017.webp",
        "name": "Momunofu",
        "chance": 6
    },
    {
        "image": "./assets/018.webp",
        "name": "Sui-Ki",
        "chance": 5
    },
    {
        "image": "./assets/019.webp",
        "name": "Parvati",
        "chance": 2
    },
    {
        "image": "./assets/020.webp",
        "name": "Beelzebub",
        "chance": 3
    },
]


# region Funções
# Printa uma imagem no console
def printImage(imgPath: str):
    image = Image.open(imgPath)
    plt.imshow(image)
    plt.axis('off')  # Hide axis
    plt.show()


# Seleciona um inimigo aleatório da lista
def getRandomEnemy():
    weights = [enemy["chance"] for enemy in enemies]
    random_object = random.choices(enemies, weights=weights, k=1)[0]

    printImage(random_object["image"])

    print(f"ATENÇÃO!")
    print(f"{random_object["name"]} apareceu!")


# Gera as combinações únicas para determinar o array de entrada
def generate_combinations(length):
    combinations = []
    for i in range(2 ** length):
        combination = [int(x) for x in bin(i)[2:].zfill(length)]
        combinations.append(combination)
    return combinations


# gera as respostas para as combinações
def generate_responses(combinations):
    responses = []
    for combination in combinations:
        response = min(sum(combination) + 1, 7)
        responses.append(response)

    return responses

# endregion


# region Enemy
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
    [1, 0, 0, 1],  # 2
    [1, 0, 1, 0],  # 2
    [0, 1, 1, 0],  # 3
    [0, 1, 0, 1],  # 3
    [0, 0, 1, 1],  # 3
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
    2,
    2,
    3,
    3,
    3,
    4,
    5,
    5,
    6,
    7
]

# Definição da rede neural
enemyAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(150, 150),
                        random_state=1)
# Treina a rede neural para encaixar os dois arrays
enemyAI.fit(enemyEntry, enemyStrength)
print("Rede Neural Inimigo Treinada!")
# endregion


# region Player
# As entradas para as informações do player seguem a seguinte ordem:
# Col 1 = Armado
# Col 2 = Armadura
# Col 3 = Afinidade a Magia
# Col 4 = Afinidade Física
# Col 5 = Melhoria no Ataque
# Col 6 = Melhoria no Agilidade
# Col 7 = Possuí Acessórios que o fortalecem
# Col 8 = Conhecimento em negociação
playerEntry = generate_combinations(8)

# Resultado de acordo com as propriedades informadas do player
# 1 = Muito Fraco
# 7 = Muito Forte
playerStrength = generate_responses(playerEntry)

# Definição da rede neural
playerAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(250, 250),
                         random_state=1)
# Treina a rede neural para encaixar os dois arrays
playerAI.fit(playerEntry, playerStrength)
print("Rede Neural Player Treinada!")
# endregion


# region PlayerCondition
# As entradas para as informações da condição do player seguem a seguinte ordem:
# Col 1 - Envenenado
# Col 2 - Encantado
# Col 3 - Confuso
# Col 4 - Amaldiçoado
# Col 5 - Poucos Pontos de Vida
# Col 6 - Poucos Pontos de Mana
playerConditionEntry = generate_combinations(6)


# Resultado de acordo com as propriedades informadas do player
# 1 = Condição Boa
# 7 = Condição Ruim
playerConditionResponse = generate_responses(playerConditionEntry)


# Definição da rede neural
playerConditionAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(250, 250),
                        random_state=1)
# Treina a rede neural para encaixar os dois arrays
playerConditionAI.fit(playerConditionEntry, playerConditionResponse)
print("Rede Neural Player Condition Treinada!")
# endregion


actionLabel = [
    "FUGIR",
    "ATACAR",
    "CURAR",
    "ATACAR COM MAGIA",
    "NEGOCIAR",
]

# Lista de string com questões para iterar abaixo
questions = [
    "está armado?",
    "está vestindo armadura?",
    "tem resistencia mágica?",
    "é grande?",
    "está armado?",
    "está vestindo armadura?",
    "possuí afinidade a mágia?",
    "possuí afinidade a dano físico?",
    "possuí uma melhoria no ataque?",
    "possuí uma melhoria na agilidade?",
    "possuí acessórios que o fortalecem?",
    "possui conhecimento com negociações?",
    "está envenenado?",
    "está encantado?",
    "está confuso?",
    "está amaldiçoado?",
    "está com poucos pontos de vida?",
    "está com poucos pontos de mana?"
]

print("\n")

getRandomEnemy()

print("\n")
# Array com os valores inseridos
searchQuery = []
# Posição de index de qual pergunta é a atual
questionPosition = 0
# O tamanho do array de pesquisa precisa ser 4 (mesma quantidade de colunas da matriz enemyEntry
while len(searchQuery) < 18:
    # define a variável option primeiro, para evitar que qualquer valor além de 1 ou 0 seja inserido
    option = -1
    if len(searchQuery) < 4:
        while option != 0 and option != 1:
            option = int(input(f"O inimigo {questions[questionPosition]}\n"))
    else:
        while option != 0 and option != 1:
            option = int(input(f"Você {questions[questionPosition]}\n"))

    # Adiciona o valor digitado de option para o array de search query
    searchQuery.append(option)
    # Muda a posição do index de pergunta para a próxima da lista
    questionPosition += 1

# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1], Resposta: [7]
enemyResult = enemyAI.predict([searchQuery[0:4]])
# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1,1,1,1,1], Resposta: [7, 1]
resultPlayer = playerAI.predict([searchQuery[4:12]])
# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1,1,1], Resposta: [7]
resultPlayerCondition = playerConditionAI.predict([searchQuery[12:18]])

print("\n")

# Calcula a diferença de poder entre o inimigo e o player
playerStrengthDiff = resultPlayer[0] - enemyResult[0]

# TODO: implementar retorno inteligente
if resultPlayer > 0:
    print(actionLabel[1])
elif playerStrengthDiff < 0:
    print(actionLabel[0])
else:
    print(actionLabel[-1])


