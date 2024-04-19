# definição de classe para formatação na hora de imprimir informações na tela
class ANSI:
    END = '\033[0m' # finalização da linha
    BOLD = '\033[1m' # deixa texto em negrito
    UNDERLINE = '\033[4m' # deixa texto com uma linha


# Dados dos inimigos para ilustrar a aplicação
enemyData = [
    {
        "image": "./assets/001.png",
        "name": "Jack Frost",
        "chance": 10
    },
    {
        "image": "./assets/002.png",
        "name": "Jack-o-Lantern",
        "chance": 10
    },
    {
        "image": "./assets/003.png",
        "name": "Pixie",
        "chance": 10
    },
    {
        "image": "./assets/004.png",
        "name": "Lucifer",
        "chance": 0.25
    },
    {
        "image": "./assets/005.png",
        "name": "Vishnu",
        "chance": 2.5
    },
    {
        "image": "./assets/006.png",
        "name": "Angel",
        "chance": 10
    },
    {
        "image": "./assets/007.png",
        "name": "Daemon",
        "chance": 10
    },
    {
        "image": "./assets/008.png",
        "name": "Slime",
        "chance": 10
    },
    {
        "image": "./assets/009.png",
        "name": "Metatron",
        "chance": 1
    },
    {
        "image": "./assets/010.png",
        "name": "Chimera",
        "chance": 8
    },
    {
        "image": "./assets/011.png",
        "name": "Cerberus",
        "chance": 5
    },
    {
        "image": "./assets/012.png",
        "name": "Hecatoncheires",
        "chance": 6
    },
    {
        "image": "./assets/013.png",
        "name": "Mada",
        "chance": 7
    },
    {
        "image": "./assets/014.png",
        "name": "Loki",
        "chance": 3
    },
    {
        "image": "./assets/015.png",
        "name": "Thor",
        "chance": 4
    },
    {
        "image": "./assets/016.png",
        "name": "Shiva",
        "chance": 0.9
    },
    {
        "image": "./assets/017.png",
        "name": "Momunofu",
        "chance": 6
    },
    {
        "image": "./assets/018.png",
        "name": "Sui-Ki",
        "chance": 5
    },
    {
        "image": "./assets/019.png",
        "name": "Parvati",
        "chance": 2
    },
    {
        "image": "./assets/020.png",
        "name": "Beelzebub",
        "chance": 3
    },
    {
        "image": "./assets/021.png",
        "name": "YHVH",
        "chance": 0.2
    },
    {
        "image": "./assets/022.png",
        "name": "Mastema",
        "chance": 1
    },
    {
        "image": "./assets/023.png",
        "name": "Onmoraki",
        "chance": 10
    },
    {
        "image": "./assets/024.png",
        "name": "Demoneeho",
        "chance": 5
    },
    {
        "image": "./assets/025.png",
        "name": "Sandalphon",
        "chance": 2
    },
]

# Input que indica a diferença de força entre inimigo/player (varia de 7 a -7)
# e a saúde do jogador (varia de 1 = boa a 7 = ruim)
actionInputData = [
    [-7, 1],
    [-7, 2],
    [-7, 3],
    [-7, 4],
    [-7, 5],
    [-7, 6],
    [-7, 7],
    [-6, 1],
    [-6, 2],
    [-6, 3],
    [-6, 4],
    [-6, 5],
    [-6, 6],
    [-6, 7],
    [-5, 1],
    [-5, 2],
    [-5, 3],
    [-5, 4],
    [-5, 5],
    [-5, 6],
    [-5, 7],
    [-4, 1],
    [-4, 2],
    [-4, 3],
    [-4, 4],
    [-4, 5],
    [-4, 6],
    [-4, 7],
    [-3, 1],
    [-3, 2],
    [-3, 3],
    [-3, 4],
    [-3, 5],
    [-3, 6],
    [-3, 7],
    [-2, 1],
    [-2, 2],
    [-2, 3],
    [-2, 4],
    [-2, 5],
    [-2, 6],
    [-2, 7],
    [-1, 1],
    [-1, 2],
    [-1, 3],
    [-1, 4],
    [-1, 5],
    [-1, 6],
    [-1, 7],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    [0, 7],
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [1, 6],
    [1, 7],
    [2, 1],
    [2, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [2, 6],
    [2, 7],
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    [3, 7],
    [4, 1],
    [4, 2],
    [4, 3],
    [4, 4],
    [4, 5],
    [4, 6],
    [4, 7],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
    [5, 5],
    [5, 6],
    [5, 7],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [6, 6],
    [6, 7],
    [7, 1],
    [7, 2],
    [7, 3],
    [7, 4],
    [7, 5],
    [7, 6],
    [7, 7],
]

# Retorna um index de label de ação
# 0 = Fugir
# 1 = Atacar
# 2 = Curar
# 3 = Negociar
actionResultData = [
    # - 7
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    # -6
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    # -5
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    # -4
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    # -3
    3,
    3,
    3,
    3,
    0,
    0,
    0,
    # -2
    1,
    3,
    3,
    2,
    2,
    0,
    0,
    # -1
    1,
    3,
    3,
    2,
    2,
    2,
    0,
    # 0
    1,
    3,
    3,
    3,
    2,
    2,
    2,
    # 1
    1,
    1,
    3,
    3,
    3,
    2,
    2,
    # 2
    1,
    1,
    3,
    3,
    3,
    2,
    2,
    # 3
    1,
    1,
    1,
    3,
    3,
    2,
    2,
    # 4
    1,
    1,
    1,
    3,
    3,
    2,
    2,
    # 5
    1,
    1,
    1,
    1,
    3,
    2,
    2,
    # 6
    1,
    1,
    1,
    1,
    1,
    3,
    2,
    # 7
    1,
    1,
    1,
    1,
    1,
    1,
    2,
]
