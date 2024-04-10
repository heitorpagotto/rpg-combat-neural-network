from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


# Gera as 256 combinações únicas para determinar o array de playerEntry
def generateBinaryCombinations(length):
    combinations = []
    for i in range(2 ** length):
        combination = [int(x) for x in bin(i)[2:].zfill(length)]
        combinations.append(combination)
    return combinations


# gera as respostas para as 256 combinações
def generateBinaryResponses(combinations):
    responses = []
    for combination in combinations:
        response = min(sum(combination) + 1, 7)  # Add 1 since responses start from 1
        responses.append(response)
    return responses


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
print("Rede Neural Treinada!")

# Lista de string com questões para iterar abaixo
questions = [
    "está armado?",
    "está vestindo armadura?",
    "possuí afinidade com mágia?",
    "possuí afinidade com dano físico?",
    "possuí uma melhoria no ataque?",
    "possuí uma melhoria na agilidade?",
    "possuí acessórios que o fortalecem?",
    "possui conhecimento com negociações?",
]

# Array com os valores inseridos
searchQuery = []
# Posição de index de qual pergunta é a atual
questionPosition = 0
# O tamanho do array de pesquisa precisa ser 8 (mesma quantidade de colunas da matriz playerEntry)
while len(searchQuery) < 8:
    # define a variável option primeiro, para evitar que qualquer valor além de 1 ou 0 seja inserido
    option = -1
    while option != 0 and option != 1:
        option = int(input(f"Você {questions[questionPosition]}\n"))

    # Adiciona o valor digitado de option para o array de search query
    searchQuery.append(option)
    # Muda a posição do index de pergunta para a próxima da lista
    questionPosition += 1

# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1,1,1,1,1], Resposta: [7]
result = playerAI.predict([searchQuery])
print(result)
