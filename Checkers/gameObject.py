# Generated by Creer at 03:55PM on April 26, 2015 UTC, git hash: '2acbba9c4b682c4de68840c1ca9bec631e9c635f'
# This is a simple class to represent the GameObject object in the game. You can extend it by adding utility functions here in this file.

from utilities import make_command
from baseGameObject import BaseGameObject


# @class GameObject: An object in the game. The most basic class that all game classes should inherit from automatically.
class GameObject(BaseGameObject):
    # initializes a GameObject with basic logic as provided by the Creer code generator
    def __init__(self):
        BaseGameObject.__init__(self)


        # The following values should get overridden when delta states are merged, but we set them here as a reference for you to see what variables this class has.

        # A unique id for each instance of a GameObject or a sub class. Used for client and server communication. Should never change value after being set.
        self.id = ""
        # Any strings logged will be stored here when this game object logs the strings. Intended for debugging.
        self.logs = []



    ## adds a message to this game object's log. Intended for debugging purposes.
    # @param <string> message: A string to add to this GameObject's log. Intended for debugging.
    def log(self, message):
        return make_command(self, 'log', message=message)
