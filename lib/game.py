import copy
import random

player = {"name": None, "balance": 100, "cards_on_hands": []}
computer_player = {"name": "Banker", "balance": 1000000, "cards_on_hands": []}
game = {"deck": []}

cards = [
    # Модель данных
    # Карты двойки
    {"name": "two", "color": "hearts", "view": "2", "colorView": "H", "value": 2},
    {"name": "two", "color": "diamonds", "view": "2", "colorView": "D", "value": 2},
    {"name": "two", "color": "clubs", "view": "2", "colorView": "C", "value": 2},
    {"name": "two", "color": "spades", "view": "2", "colorView": "S", "value": 2},
    # Карты тройки
    {"name": "three", "color": "hearts", "view": "3", "colorView": "H", "value": 3},
    {"name": "three", "color": "diamonds", "view": "3", "colorView": "D", "value": 3},
    {"name": "three", "color": "clubs", "view": "3", "colorView": "C", "value": 3},
    {"name": "three", "color": "spades", "view": "3", "colorView": "S", "value": 3},
    # Карты четверки
    {"name": "four", "color": "hearts", "view": "4", "colorView": "H", "value": 4},
    {"name": "four", "color": "diamonds", "view": "4", "colorView": "D", "value": 4},
    {"name": "four", "color": "clubs", "view": "4", "colorView": "C", "value": 4},
    {"name": "four", "color": "spades", "view": "4", "colorView": "S", "value": 4},
    # Карты пятерки
    {"name": "five", "color": "hearts", "view": "5", "colorView": "H", "value": 5},
    {"name": "five", "color": "diamonds", "view": "5", "colorView": "D", "value": 5},
    {"name": "five", "color": "clubs", "view": "5", "colorView": "C", "value": 5},
    {"name": "five", "color": "spades", "view": "5", "colorView": "S", "value": 5},
    # Карты шестерки
    {"name": "six", "color": "hearts", "view": "6", "colorView": "H", "value": 6},
    {"name": "six", "color": "diamonds", "view": "6", "colorView": "D", "value": 6},
    {"name": "six", "color": "clubs", "view": "6", "colorView": "C", "value": 6},
    {"name": "six", "color": "spades", "view": "6", "colorView": "S", "value": 6},
    # Карты семерки
    {"name": "seven", "color": "hearts", "view": "7", "colorView": "H", "value": 7},
    {"name": "seven", "color": "diamonds", "view": "7", "colorView": "D", "value": 7},
    {"name": "seven", "color": "clubs", "view": "7", "colorView": "C", "value": 7},
    {"name": "seven", "color": "spades", "view": "7", "colorView": "S", "value": 7},
    # Карты восьмерки
    {"name": "eight", "color": "hearts", "view": "8", "colorView": "H", "value": 8},
    {"name": "eight", "color": "diamonds", "view": "8", "colorView": "D", "value": 8},
    {"name": "eight", "color": "clubs", "view": "8", "colorView": "C", "value": 8},
    {"name": "eight", "color": "spades", "view": "8", "colorView": "S", "value": 8},
    # Карты девятки
    {"name": "nine", "color": "hearts", "view": "9", "colorView": "H", "value": 9},
    {"name": "nine", "color": "diamonds", "view": "9", "colorView": "D", "value": 9},
    {"name": "nine", "color": "clubs", "view": "9", "colorView": "C", "value": 9},
    {"name": "nine", "color": "spades", "view": "9", "colorView": "S", "value": 9},
    # Карты десятки
    {"name": "ten", "color": "hearts", "view": "X", "colorView": "H", "value": 10},
    {"name": "ten", "color": "diamonds", "view": "X", "colorView": "D", "value": 10},
    {"name": "ten", "color": "clubs", "view": "X", "colorView": "C", "value": 10},
    {"name": "ten", "color": "spades", "view": "X", "colorView": "S", "value": 10},
    # Карты вальты
    {"name": "jack", "color": "hearts", "view": "J", "colorView": "H", "value": 10},
    {"name": "jack", "color": "diamonds", "view": "J", "colorView": "D", "value": 10},
    {"name": "jack", "color": "clubs", "view": "J", "colorView": "C", "value": 10},
    {"name": "jack", "color": "spades", "view": "J", "colorView": "S", "value": 10},
    # Карты дамы
    {"name": "queen", "color": "hearts", "view": "Q", "colorView": "H", "value": 10},
    {"name": "queen", "color": "diamonds", "view": "Q", "colorView": "D", "value": 10},
    {"name": "queen", "color": "clubs", "view": "Q", "colorView": "C", "value": 10},
    {"name": "queen", "color": "spades", "view": "Q", "colorView": "S", "value": 10},
    # Карты короли
    {"name": "king", "color": "hearts", "view": "K", "colorView": "H", "value": 10},
    {"name": "king", "color": "diamonds", "view": "K", "colorView": "D", "value": 10},
    {"name": "king", "color": "clubs", "view": "K", "colorView": "C", "value": 10},
    {"name": "king", "color": "spades", "view": "K", "colorView": "S", "value": 10},
    # Тузы
    {"name": "ace", "color": "hearts", "view": "A", "colorView": "H", "value": 11},
    {"name": "ace", "color": "diamonds", "view": "A", "colorView": "D", "value": 11},
    {"name": "ace", "color": "clubs", "view": "A", "colorView": "C", "value": 11},
    {"name": "ace", "color": "spades", "view": "A", "colorView": "S", "value": 11},
]

def play():
    print_menu()
    game["deck"] = get_deck()
    player_turn()

    if bust(player["cards_on_hands"]):
        print("============================================")
        print("Game Over YOU LOSE!!! :)")
        print("============================================")
        return

    computer_turn()
    player_win, computer_player_win = compare_cards()
    print_computer_cards()

    print("============================================")
    if player_win > computer_player_win:
        print("Вы победили!!!")
    elif computer_player_win > player_win:
        print("Game Over YOU LOSE!!! :)")
    else:
        print("Ничья Братан!!! :)")
    print("============================================")

def player_turn():
    answer = "yes"
    player["cards_on_hands"].append(game["deck"].pop())  # Ложим 2 карту в руки пользователя

    while answer[0].lower() == "y":
        player["cards_on_hands"].append(game["deck"].pop())  # Ложим 1 карту в руки пользователя
        print_player_cards()
        if bust(player["cards_on_hands"]) or black_jack(player["cards_on_hands"]):
            break
        answer = input("Вам нужна еще карта?: ")

def computer_turn():
    while eval_aces(computer_player["cards_on_hands"]) < 18:
        computer_player["cards_on_hands"].append(game["deck"].pop())  # Ложим 2 карту в руки computer_player

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

def draw_cards(cards):
    lines = ["", "", "", "", ""]
    for card in cards:
        lines[0] = lines[0] + "  " + "%s--------%s" % (card["colorView"], card["colorView"])
        lines[1] = lines[1] + "  " + "| %s      |" % card["view"]
        lines[2] = lines[2] + "  " + "|        |"
        lines[3] = lines[3] + "  " + "|      %s |" % card["view"]
        lines[4] = lines[4] + "  " + "%s--------%s" % (card["colorView"], card["colorView"])
    for line in lines:
        print(line)

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

    draw_cards(player["cards_on_hands"])

def print_computer_cards():
    print("============================================")
    print("%s имеет на руках" % computer_player["name"])
    print("============================================")

    draw_cards(computer_player["cards_on_hands"])

def sum(hand):
    value = 0
    for card in hand:
        value = value + card["value"]
    return value

def eval_aces(hand):
    value = sum(hand)
    for card in hand:
        if value > 21 and card["name"] == "ace":
            card["value"] = 1
            value = sum(hand)
    return value

def black_jack(hand):
    value = eval_aces(hand)
    if value == 21:
        return True
    else:
        return False

def bust(hand):
    value = eval_aces(hand)
    if value > 21:
        return True
    else:
        return False

def balance(player, val):
    player["balance"] = player["balance"] + val
    return player["balance"]

def compare_cards():
    player_win = 0
    computer_player_win = 0
    # Получение очков играков
    player_scores = eval_aces(player["cards_on_hands"])
    computer_player_scores = eval_aces(computer_player["cards_on_hands"])

    # проверка на проиграш
    is_player_busted = bust(player["cards_on_hands"])
    is_computer_player_busted = bust(computer_player["cards_on_hands"])

    # проверка на black jack
    is_player_black_jack = black_jack(player["cards_on_hands"])
    is_computer_player_black_jack = black_jack(computer_player["cards_on_hands"])

    if is_player_busted:
        if not is_computer_player_black_jack and computer_player_scores < 21:
            computer_player_win += 1

    if is_computer_player_busted:
        if not is_player_black_jack and player_scores < 21:
            player_win += 1

    if is_computer_player_busted and is_player_busted:
        if player_scores > computer_player_scores:
            player_win += 1
        elif computer_player_scores > player_scores:
            computer_player_win += 1
        else:
            player_win += 1
            computer_player_win += 1

    if is_player_black_jack:
        player_win += 1

    if is_computer_player_black_jack:
        computer_player_win += 1

    if is_player_black_jack and is_computer_player_black_jack:
        player_win += 1
        computer_player_win += 1

    if player_scores < 21 and computer_player_scores < 21:
        if player_scores > computer_player_scores:
            player_win += 1
        elif computer_player_scores > player_scores:
            computer_player_win += 1
        else:
            player_win += 1
            computer_player_win += 1

    return player_win, computer_player_win