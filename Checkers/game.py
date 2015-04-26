# Generated by Creer at 03:55PM on April 26, 2015 UTC, git hash: '2acbba9c4b682c4de68840c1ca9bec631e9c635f'
# This is a simple class to represent the Game object in the game. You can extend it by adding utility functions here in this file.

from utilities import make_command
from baseGame import BaseGame

# import game objects
from Checkers.checker import Checker
from Checkers.player import Player
from Checkers.gameObject import GameObject

# @class Game: The simple version of American Checkers. An 8x8 board with 12 checkers on each side that must move diagonally to the opposing side until kinged. Very simple.
class Game(BaseGame):
    # initializes a Game with basic logic as provided by the Creer code generator
    def __init__(self):
        BaseGame.__init__(self)


        # The following values should get overridden when delta states are merged, but we set them here as a reference for you to see what variables this class has.

        # All the checkers currently in the game.
        self.checkers = []
        # The player whose turn it is currently. That player can send commands. Other players cannot.
        self.current_player = None
        # A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        self.game_objects = {}
        # The height of the board for the Y component of a checker.
        self.board_height = 8
        # The checker that last moved and must be moved because only one checker can move during each players turn.
        self.checker_moved = None
        # List of all the players in the game.
        self.players = []
        # The maximum number of turns before the game will automatically end.
        self.max_turns = 100
        # If the last checker that moved jumped, meaning it can move again.
        self.checker_moved_jumped = False
        # The width of the board for X component of a checker.
        self.board_width = 8
        # The current turn number, starting at 0 for the first player's turn
        self.current_turn = 0

        self.name = "Checkers"

        self._game_object_classes = {
            'Checker': Checker,
            'Player': Player,
            'GameObject': GameObject
        }

