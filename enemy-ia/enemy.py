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
    [1],
    [1],
    [1],
    [1],
    [2],
    [2],
    [2],
    [2],
    [3],
    [3],
    [3],
    [4],
    [5],
    [5],
    [6],
    [7]
]

enemyAI = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-8, hidden_layer_sizes=(20, 20), random_state=1)
