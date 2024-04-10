from sklearn.neural_network import MLPClassifier


# Gera as 64 combinações únicas para determinar o array de playerConditionEntry
def generateBinaryCombinations(length):
    combinations = []
    for i in range(2 ** length):
        combination = [int(x) for x in bin(i)[2:].zfill(length)]
        combinations.append(combination)
    return combinations


# gera as respostas para as 64 combinações
def generateBinaryResponses(combinations):
    responses = []
    for combination in combinations:
        response = min(sum(combination) + 1, 7)  # Add 1 since responses start from 1
        responses.append(response)
    return responses


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
print("Rede Neural Treinada!")

# Lista de string com questões para iterar abaixo
questions = [
    "está envenenado?",
    "está encantado?",
    "está desnorteado?",
    "está amaldiçoado?",
    "está com poucos pontos de vida?",
    "está com poucos pontos de mana?"
]

# Array com os valores inseridos
searchQuery = []
# Posição de index de qual pergunta é a atual
questionPosition = 0
# O tamanho do array de pesquisa precisa ser 8 (mesma quantidade de colunas da matriz playerEntry)
while len(searchQuery) < 6:
    # define a variável option primeiro, para evitar que qualquer valor além de 1 ou 0 seja inserido
    option = -1
    while option != 0 and option != 1:
        option = int(input(f"Você {questions[questionPosition]}\n"))

    # Adiciona o valor digitado de option para o array de search query
    searchQuery.append(option)
    # Muda a posição do index de pergunta para a próxima da lista
    questionPosition += 1

# Faz a busca e pega o resultado da IA
# EX: [1,1,1,1,1,1], Resposta: [7]
result = playerConditionAI.predict([searchQuery])
print(result)
