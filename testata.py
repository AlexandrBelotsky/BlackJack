import random
import time


sp = list(range(2, 11)) * 4
sp1 = ['J', 'Q', 'K', 'A'] * 4
sp.extend(sp1)
value = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
          8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 10}

player_card = []
Bot_card = []
dealer_card = []

def start_two():
    for i in range(2):
        card = random.choice(sp)
        player_card.append(card)
        sp.remove(card)
        card = random.choice(sp)
        dealer_card.append(card)
        sp.remove(card)
    print(f"Карты диллера {dealer_card[0]} X")
    print(f"Твои карты {player_card[0]} {player_card[1]} Очков: {sum(map(value.get, player_card))}")
    while True:
            what = input("Взять карту\nПас\n1/2: ")
            if what == '1':
                return take()
            elif what == '2':
                pass
            else:
                print("Введите корректное значение")
            continue

def take():
    card = random.choice(sp)
    player_card.append(card)
    sp.remove(card)
    print(f"Твои карты {player_card[0]} {player_card[1]} {player_card[2]} Очков: {sum(map(value.get, player_card))}")





start_two()