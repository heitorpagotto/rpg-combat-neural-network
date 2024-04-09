from sklearn.neural_network import MLPClassifier
from PIL import Image
import matplotlib.pyplot as plt
import random
from data import actionResultData, actionInputData, enemyData, ANSI

# Dados dos inimigos para ilustrar a aplicação
enemies = enemyData


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

    print(f"\n{ANSI.BOLD}ATENÇÃO!{ANSI.END}\n")
    print(f"{ANSI.UNDERLINE}{random_object["name"]}{ANSI.END} apareceu!")


# Gera combinações binárias únicas para determinar o array de entrada
def generateBinaryCombinations(length):
    combinations = []
    for i in range(2 ** length):
        combination = [int(x) for x in bin(i)[2:].zfill(length)]
        combinations.append(combination)
    return combinations


# gera as respostas para as combinações binárias
def generateBinaryResponses(combinations):
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
playerEntry = generateBinaryCombinations(8)

# Resultado de acordo com as propriedades informadas do player
# 1 = Muito Fraco
# 7 = Muito Forte
playerStrength = generateBinaryResponses(playerEntry)

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
playerConditionEntry = generateBinaryCombinations(6)


# Resultado de acordo com as propriedades informadas do player
# 1 = Condição Boa
# 7 = Condição Ruim
playerConditionResponse = generateBinaryResponses(playerConditionEntry)


# Definição da rede neural
playerConditionAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(250, 250),
                        random_state=1)
# Treina a rede neural para encaixar os dois arrays
playerConditionAI.fit(playerConditionEntry, playerConditionResponse)
print("Rede Neural Player Condition Treinada!")
# endregion


# region ActionAI
# Input que indica a diferença de força entre inimigo/player (varia de 7 a -7)
# e a saúde do jogador (varia de 1 = boa a 7 = ruim)
playerActionInput = actionInputData
# Retorna um index de label de ação
playerActionResponse = actionResultData

# Define a rede que irá responder com um index de label de ação
actionAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(400, 400),
                         random_state=1)
# Treina a rede neural para encaixar os dois arrays
actionAI.fit(playerActionInput, playerActionResponse)
print("Rede Neural Player Action Treinada!")
# endregion

actionLabel = [
    "FUGIR",
    "ATACAR",
    "CURAR",
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

while True:
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

    # Prevê qual ação se deve tomar baseado na diferença de força e a condição do player
    actionResult = actionAI.predict([[playerStrengthDiff, resultPlayerCondition[0]]])

    print(f"{ANSI.UNDERLINE}A melhor ação é:{ANSI.END}")
    print(f"{ANSI.BOLD}{actionLabel[actionResult[0]]}{ANSI.END}")
