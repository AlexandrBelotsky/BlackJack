import random
import time

sp = list(range(2, 11)) * 4
sp1 = ['J', 'Q', 'K', 'A'] * 4
sp.extend(sp1)
value = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
          8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 10}

player_cart = []
player_cart2 = []
player_cart3 = []
player_cart4 = []
dealer_cart = []
game = [player_cart, dealer_cart, player_cart2, player_cart3, player_cart4]

class Player:

    while True:
        how = input("Введите количевство игроков(1/2/3/4): ")
        if how == '1':
            game.remove(player_cart2)
            game.remove(player_cart3)
            game.remove(player_cart4)
            break
        elif how == '2':
            game.remove(player_cart3)
            game.remove(player_cart4)
            break
        elif how == '3':
            game.remove(player_cart4)
            break
        elif how == '4':
            pass
            break
        else:
            print("Введите корректное значение")
            continue


class Game(Player):

    n = 2
    while n != 0:
        card = random.choice(sp)
        game[0].append(card)
        sp.remove(card)
        card = random.choice(sp)
        game[1].append(card)
        sp.remove(card)
        n -= 1
    print(f"Твои карты: {game[0][0]} {game[0][1]} Очков: {sum(map(value.get, game[0]))}")
    print(f"Карты диллера: {game[1][0]} X")
    question = input("1)Взять карту 2)Не брать: ")
    if question == '1':
        card = random.choice(sp)
        game[0].append(card)
        sp.remove(card)
        a = sum(map(value.get, game[0]))
        b = sum(map(value.get, game[1]))
        print(f"Твои карты: {game[0][0]} {game[0][1]} {game[0][2]} Очков: {a}")
        if a > 21:
            print(f"У тебя перебор, ты проиграл")
        elif a < 21:
            question = input("1)Взять карту 2)Не брать: ")


        elif a == 21:
            print("'BlackJack' Поздравляем ты выиграл")


    elif question == '2':
        card = random.choice(sp)
        game[1].append(card)
        sp.remove(card)
        b = sum(map(value.get, game[1]))
        if b < 21:
            print(f"Карты диллера: {game[1][0]} {game[1][1]} X")
            time.sleep(1)
            card = random.choice(sp)
            game[1].append(card)
            sp.remove(card)
            b = sum(map(value.get, game[1]))
            if b > 21:
                print(f"Карты диллера: {game[1][0]} {game[1][1]} {game[1][2]} {game[1][3]} Очков: {b}")
                print(f"У диллера перебор, ты выиграл")
            elif b == 21:
                print(f"Карты диллера: {game[1][0]} {game[1][1]} {game[1][2]} {game[1][3]} Очков: {b}")
                print(f"BlackJack Диллер выиграл")

        elif b > 21:
            print(f"Карты диллера: {game[1][0]} {game[1][1]} {game[1][2]} Очки: {b}\n"
                  f"У диллера перебор. Ты выиграл")
        elif b == 21:
            print(f"Карты диллера: {game[1][0]} {game[1][1]} {game[1][2]} Очки: {b}\n"
                  f"BlackJack Диллер выиграл")














a = Player()






