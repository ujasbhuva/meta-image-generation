# import requests

# response = requests.get("http://127.0.0.1:8000/profile-pic-url-hd", params={"username": "alexandradaddario"}, headers={"Authorization" : "c3PdB6ttMJv6t9f4b7k5gv8qTxoSbpzR0mU5O32p"})

# print(response.content)

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()

class Dealer:
    def __init__(self, deck):
        self.deck = deck

    def issue_initial_cards(self, players):
        for player in players:
            face_down_card = self.deck.draw_card()
            face_up_card = self.deck.draw_card()
            player.receive_cards([face_down_card, face_up_card])

    def issue_additional_card(self, player):
        print(
            ">>> The dealer is issuing an additional card to you. <<<"
        )
        additional_card = self.deck.draw_card()
        player.receive_cards([additional_card])

class Player:
    def __init__(self):
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def ask_for_another_card(self):
        return input("Do you want another card? (yes/no): ").lower() == 'yes'

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.players = [Player(), Player()]

    def start_game(self):
        self.dealer.issue_initial_cards(self.players)
        for player in self.players:
            while player.ask_for_another_card():
                self.dealer.issue_additional_card(player)

if __name__ == "__main__":
    game = Game()
    game.start_game()
