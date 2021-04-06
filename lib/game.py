import copy
import random

player = {"name": None, "balance": 100, "cards_on_hands": []}
computer_player = {"name": "Banker", "balance": 1000000, "cards_on_hands": []}
game = {"deck": []}

cards = [
    # Модель данных
    # Карты двойки
    {"name": "two", "color": "hearts", "view": "2", "colorView": "♥", "value": 2},
    {"name": "two", "color": "diamonds", "view": "2", "colorView": "♦", "value": 2},
    {"name": "two", "color": "clubs", "view": "2", "colorView": "♣", "value": 2},
    {"name": "two", "color": "spades", "view": "2", "colorView": "♠", "value": 2},
    # Карты тройки
    {"name": "three", "color": "hearts", "view": "3", "colorView": "♥", "value": 3},
    {"name": "three", "color": "diamonds", "view": "3", "colorView": "♦", "value": 3},
    {"name": "three", "color": "clubs", "view": "3", "colorView": "♣", "value": 3},
    {"name": "three", "color": "spades", "view": "3", "colorView": "♠", "value": 3},
    # Карты четверки
    {"name": "four", "color": "hearts", "view": "4", "colorView": "♥", "value": 4},
    {"name": "four", "color": "diamonds", "view": "4", "colorView": "♦", "value": 4},
    {"name": "four", "color": "clubs", "view": "4", "colorView": "♣", "value": 4},
    {"name": "four", "color": "spades", "view": "4", "colorView": "♠", "value": 4},
    # Карты пятерки
    {"name": "five", "color": "hearts", "view": "5", "colorView": "♥", "value": 5},
    {"name": "five", "color": "diamonds", "view": "5", "colorView": "♦", "value": 5},
    {"name": "five", "color": "clubs", "view": "5", "colorView": "♣", "value": 5},
    {"name": "five", "color": "spades", "view": "5", "colorView": "♠", "value": 5},
    # Карты шестерки
    {"name": "six", "color": "hearts", "view": "6", "colorView": "♥", "value": 6},
    {"name": "six", "color": "diamonds", "view": "6", "colorView": "♦", "value": 6},
    {"name": "six", "color": "clubs", "view": "6", "colorView": "♣", "value": 6},
    {"name": "six", "color": "spades", "view": "6", "colorView": "♠", "value": 6},
    # Карты семерки
    {"name": "seven", "color": "hearts", "view": "7", "colorView": "♥", "value": 7},
    {"name": "seven", "color": "diamonds", "view": "7", "colorView": "♦", "value": 7},
    {"name": "seven", "color": "clubs", "view": "7", "colorView": "♣", "value": 7},
    {"name": "seven", "color": "spades", "view": "7", "colorView": "♠", "value": 7},
    # Карты восьмерки
    {"name": "eight", "color": "hearts", "view": "8", "colorView": "♥", "value": 8},
    {"name": "eight", "color": "diamonds", "view": "8", "colorView": "♦", "value": 8},
    {"name": "eight", "color": "clubs", "view": "8", "colorView": "♣", "value": 8},
    {"name": "eight", "color": "spades", "view": "8", "colorView": "♠", "value": 8},
    # Карты девятки
    {"name": "nine", "color": "hearts", "view": "9", "colorView": "♥", "value": 9},
    {"name": "nine", "color": "diamonds", "view": "9", "colorView": "♦", "value": 9},
    {"name": "nine", "color": "clubs", "view": "9", "colorView": "♣", "value": 9},
    {"name": "nine", "color": "spades", "view": "9", "colorView": "♠", "value": 9},
    # Карты десятки
    {"name": "ten", "color": "hearts", "view": "X", "colorView": "♥", "value": 10},
    {"name": "ten", "color": "diamonds", "view": "X", "colorView": "♦", "value": 10},
    {"name": "ten", "color": "clubs", "view": "X", "colorView": "♣", "value": 10},
    {"name": "ten", "color": "spades", "view": "X", "colorView": "♠", "value": 10},
    # Карты вальты
    {"name": "jack", "color": "hearts", "view": "J", "colorView": "♥", "value": 10},
    {"name": "jack", "color": "diamonds", "view": "J", "colorView": "♦", "value": 10},
    {"name": "jack", "color": "clubs", "view": "J", "colorView": "♣", "value": 10},
    {"name": "jack", "color": "spades", "view": "J", "colorView": "♠", "value": 10},
    # Карты дамы
    {"name": "queen", "color": "hearts", "view": "Q", "colorView": "♥", "value": 10},
    {"name": "queen", "color": "diamonds", "view": "Q", "colorView": "♦", "value": 10},
    {"name": "queen", "color": "clubs", "view": "Q", "colorView": "♣", "value": 10},
    {"name": "queen", "color": "spades", "view": "Q", "colorView": "♠", "value": 10},
    # Карты короли
    {"name": "king", "color": "hearts", "view": "K", "colorView": "♥", "value": 10},
    {"name": "king", "color": "diamonds", "view": "K", "colorView": "♦", "value": 10},
    {"name": "king", "color": "clubs", "view": "K", "colorView": "♣", "value": 10},
    {"name": "king", "color": "spades", "view": "K", "colorView": "♠", "value": 10},
    # Тузы
    {"name": "ace", "color": "hearts", "view": "A", "colorView": "♥", "value": (11, 1)},# кортеж
    {"name": "ace", "color": "diamonds", "view": "A", "colorView": "♦", "value": (11, 1)},
    {"name": "ace", "color": "clubs", "view": "A", "colorView": "♣", "value": (11, 1)},
    {"name": "ace", "color": "spades", "view": "A", "colorView": "♠", "value": (11, 1)},
]

def play():
   return None

def player_turn():
   return None

def computer_turn():
    return None

def start_game():
    print_menu()# Вызов функции print_menu()
    game["deck"] = get_deck()
    player["cards_on_hands"].append(game["deck"].pop())# Ложим 1 карту в руки пользователя
    player["cards_on_hands"].append(game["deck"].pop())# Ложим 2 карту в руки пользователя

    computer_player["cards_on_hands"].append(game["deck"].pop())  # Ложим 1 карту в руки computer_player
    computer_player["cards_on_hands"].append(game["deck"].pop())  # Ложим 2 карту в руки computer_player
    print_player_cards()

def get_deck():
    deck = []
    for val in cards:
        deck.append(val.copy())# Ложим копии карт из масива (val.copy())

    random.shuffle(deck)# перемешует все в масиве random.shuffle(deck) import random
    return deck

def print_card(card):
    print("%s--------%s" % (card["colorView"], card["colorView"])) # Выводим 2 переменние  "colorView": "♠",
    print("| %s      |" % card["view"])
    print("|        |")
    print("|      %s |" % card["view"])
    print("%s--------%s" % (card["colorView"], card["colorView"]))

def print_menu():
    print("============================================")
    print("♥♦♣♠            BLACK JACK            ♥♦♣♠")
    print("============================================")
    print("Игрок 1: Пожалуйста введите свое имя")
    player["name"] = input("Имя:")
    print("Ваше имя: %s" % player["name"])
    print("Ваш баланс: %s" % player["balance"])

def print_player_cards():
    print("============================================")
    print("%s вы имеете на руках" % player["name"])
    print("============================================")

    for val in player["cards_on_hands"]:
        print_card(val)

def print_computer_cards():
    print("============================================")
    print("%s имеет на руках" % computer_player["name"])
    print("============================================")

    for val in computer_player["cards_on_hands"]:
        print_card(val)