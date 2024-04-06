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


def printImage(imgPath: str):
    image = Image.open(imgPath)
    plt.imshow(image)
    plt.axis('off')  # Hide axis
    plt.show()


def getRandomEnemy():
    weights = [enemy["chance"] for enemy in enemies]
    random_object = random.choices(enemies, weights=weights, k=1)[0]

    printImage(random_object["image"])

    print(f"ATENÇÃO!")
    print(f"{random_object["name"]} apareceu!")


getRandomEnemy()

# TODO: implementar as outras 3 redes neurais
