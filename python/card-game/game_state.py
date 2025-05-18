from typing import List
from deck import Deck
from player import Player
from card import Card

class GameState:
    """
    Represents a game of Uno
    1. Create a deck of cards
    2. Create a list of players
    3. Set a current player
    4. Set a play direction
    5. Create an empty discard pile
    6. Deal out 7 cards
    7. Add a starting top card

    game actions
    - get_top_card
    """
    def __init__(self, player_names: List[str]):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.direction = 1  # 1 = clockwise, 2 = anti-clockwise
        self.discard_pile = []

        self._deal_initial_hands()

        # starting card
        self.discard_pile.append(self.deck.draw_card())

    def _deal_initial_hands(self):
        for _ in range(7):
            for player in self.players:
                card = self.deck.draw_card()
                player.draw_card(card)

    def get_top_card(self) -> Card:
        return self.discard_pile[-1]

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def get_next_player(self) -> Player:
        next_idx = (self.current_player_index + self.direction) % len(self.players)
        return self.players[next_idx]

    def next_player(self):
        self.current_player_index = (self.current_player_index + self.direction) % len(self.players)

    def reverse_direction(self):
        self.direction *= -1
