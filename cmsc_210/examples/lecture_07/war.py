"""
Let's implement a simple card game: https://en.wikipedia.org/wiki/War_(card_game)
* Player
 - name
 - score
 - hand
 - is hand empty?
 + play a card
 + get a point

* Deck
 - cards
 + shuffle
 + deal

* Card
 - suit
 - value

* Game
 - deck
 - players
 + play

"""
from functools import total_ordering
from random import shuffle


FACES = ("Jack", "Queen", "King", "Ace")
SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")


@total_ordering
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class FaceCard(Card):

    def __init__(self, suit, face):
        value = FACES.index(face) + 11
        super().__init__(suit, value)
        self.face = face

    def __str__(self):
        return f"{self.face} of {self.suit}"


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

    def __str__(self):
        return self.name

    def is_empty(self):
        return len(self.hand) == 0

    def recieve_card(self, card):
        self.hand.append(card)

    def play(self):
        return self.hand.pop()


class Deck:

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in range(2, 11):
                self.cards.append(Card(suit, value))
            for face in FACES:
                self.cards.append(FaceCard(suit, face))
        shuffle(self.cards)

    def deal(self, players):
        while self.cards:
            for player in players:
                player.recieve_card(self.cards.pop())
                if not self.cards:
                    return


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player_1 = Player("Sid")
        self.player_2 = Player("Nancy")
        self.deck.deal([self.player_1, self.player_2])

    def can_continue(self):
        return not self.player_2.is_empty() and not self.player_1.is_empty()

    def play(self):
        while self.can_continue():
            self.play_hand()
        print(f"{self.player_1} has {self.player_1.score} | {self.player_2} has {self.player_2.score}")

    def play_hand(self):
        points = 1
        while self.can_continue():
            p1_card = self.player_1.play()
            p2_card = self.player_2.play()
            if p1_card > p2_card:
                self.player_1.score += points
                print("Player 1 wins")
                return
            elif p1_card < p2_card:
                self.player_2.score += points
                print("Player 2 wins")
                return
            else:
                print("There was a tie!")
                if not self.can_continue():
                    return
                self.player_1.play()
                self.player_2.play()
            points += 1


game = Game()
game.play()
