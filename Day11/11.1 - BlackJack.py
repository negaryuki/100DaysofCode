# Ok Lets try writing a blackjack game on my own.

import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

        return score


def compare(user_score, pc_score):
    if user_score > 21 and pc_score > 21:
        return "You went over. You lose  x_X"

    elif pc_score == user_score:
        return "It's a Draw :| "
    elif pc_score == 0:
        return "Aww you lose! the dealer has a Blackjack x_X"
    elif user_score == 0:
        return "Awesome! you've got Blackjack ! you win ^o^/"
    elif user_score > 21:
        return "Oh oh, You went over! you lose!"
    elif pc_score > 21:
        return "You win !"
    elif pc_score < user_score:
        return "You are a winner!"
    else:
        return "You Lose!"


def game_start():
    user_deck = []
    pc_deck = []
    is_game_over = False

    for i in range(2):
        user_deck.append(deal_cards())
        pc_deck.append(deal_cards())
        return user_deck, pc_deck

    while not is_game_over:
        user_score = calculate_score(user_deck)
        pc_score = calculate_score(user_deck)

        compare(user_score, pc_score)

        print(f"   Your cards: {user_deck}, current score: {user_score}")
        print(f"   Computer's first card: {pc_deck[0]}")

        if pc_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:

            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if user_should_deal == "y":
                user_deck.append(deal_cards())
            if user_score < 17:
                print("Your cards are less than 17. You have to draw a card")
                user_deck.append(deal_cards())
            if user_should_deal == "n":
                is_game_over = True

        while pc_score < 17 and pc_score != 0:
            pc_deck.append(deal_cards())
            pc_score = calculate_score(pc_deck)

        print(f"   Your final hand: {user_deck}, final score: {user_score}")
        print(f"   Computer's final hand: {pc_deck}, final score: {pc_score}")
        print(compare(user_score, pc_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    game_start()
