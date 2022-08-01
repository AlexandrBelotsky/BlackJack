import random

sp = list(range(2, 11)) * 4
sp1 = ['J', 'Q', 'K', 'A'] * 4
sp.extend(sp1)
player_cart = []
dealer_cart = []
value = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
          8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 10}

#Чтобы был активным
player = True
dealer = True


def pokazat_dealer_cart():
    if len(dealer_cart) == 2:
        return dealer_cart[0]
    elif len(dealer_cart) > 2:
        return dealer_cart[0], dealer_cart[1]
    elif len(dealer_cart) > 3:
        return dealer_cart[0], dealer_cart[1], dealer_cart[2]


def razdacha(n):
    card = random.choice(sp)
    n.append(card)
    sp.remove(card)


for _ in range(2):
    razdacha(dealer_cart)
    razdacha(player_cart)

while player or dealer:
    print(f'Карты диллера {pokazat_dealer_cart()} X')
    print(f'Твои карты {player_cart} Очки: {sum(map(value.get, player_cart))}')
    if player:
        vibor = input('1: Пас\n2: Взять\nВыбор: ')
    elif sum(map(value.get, dealer_cart)) > 16:
        dealer = False
    else:
        razdacha(dealer_cart)

    if vibor == '1':
        player = False

    else:
        razdacha(player_cart)

    if sum(map(value.get, player_cart)) >= 21:
        break

    elif sum(map(value.get, dealer_cart)) >= 21:
        break

if sum(map(value.get, player_cart)) == 21:
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))} карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('BlackJack Ты выиграл')

elif sum(map(value.get, dealer_cart)) == 21:
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))} карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('BlackJack диллер выиграл')

elif sum(map(value.get, player_cart)) > 21:
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))} карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('Ты переборщил, диллер выиграл')

elif sum(map(value.get, dealer_cart)) > 21:
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))} карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('Диллер переборщил, ты выиграл')

elif 21 - sum(map(value.get, dealer_cart)) < 21 - sum(map(value.get, player_cart)):
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))} карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('Диллер выиграл')

elif 21 - sum(map(value.get, dealer_cart)) > 21 - sum(map(value.get, player_cart)):
    print(f'\nТвои карты {player_cart} Очки:'
          f' {sum(map(value.get, player_cart))}  карты диллера {dealer_cart} Очки: {sum(map(value.get, dealer_cart))}')
    print('Ты выиграл')

else:
    print('error')
