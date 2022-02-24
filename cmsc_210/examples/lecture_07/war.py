from functools import total_ordering
from random import shuffle


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def play(self):
        return self.hand.pop()

    def receive(self, cards):
        for card in cards:
            self.hand.insert(0, card)

    def is_hand_empty(self):
        return not self.hand


FACE = ("Jack", "Queen", "King", "Ace")
SUIT = ("Club", "Spade", "Diamond", "Heart")


@total_ordering
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


class FaceCard(Card):

    def __init__(self, suit, face):
        value = FACE.index(face) + 11
        super().__init__(suit, value)
        self.face = face

    def __str__(self):
        return f"{self.face} of {self.suit}"


class Deck:

    def __init__(self):
        self.cards = []
        for suit in SUIT:
            for i in range(2, 11):
                self.cards.append(Card(suit, i))
            for face in FACE:
                self.cards.append(FaceCard(suit, face))
        shuffle(self.cards)

    def deal(self, players):
        while self.cards:
            for player in players:
                card = self.cards.pop()
                player.receive([card])
                if not self.cards:
                    return


class Game:

    def __init__(self, name_1, name_2):
        self.player_1 = Player(name_1)
        self.player_2 = Player(name_2)
        deck = Deck()
        deck.deal([self.player_1, self.player_2])

    def is_game_over(self):
        return self.player_1.is_hand_empty() or self.player_2.is_hand_empty()

    def play(self):
        previous_hands = []
        total_hands = 0
        while not self.is_game_over():
            c1 = self.player_1.play()
            c2 = self.player_2.play()
            if c1 < c2:  # player 2 is the winner
                self.player_2.receive([c1, c2] + previous_hands)
                previous_hands = []
            elif c1 > c2:
                self.player_1.receive([c1, c2] + previous_hands)
                previous_hands = []
            else:
                previous_hands.extend([c1, c2])
                for i in range(3):
                    if not self.is_game_over():
                        previous_hands.append(self.player_1.play())
                        previous_hands.append(self.player_2.play())
            total_hands += 1
        if self.player_1.is_hand_empty():
            print(f"Player {self.player_2} is the winner in {total_hands} hands.")
        else:
            print(f"Player {self.player_1} is the winner in {total_hands} hands.")
