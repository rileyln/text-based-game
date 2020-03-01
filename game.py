# Author: Riley Lynn Nairn, pronouns: she, her
# Date created: 2020 March 1
# Description: Game

class Game:
    """
    Game
    """

    # Possible game states
    UNFINISHED = "UNFINISHED"
    WIN = "WIN"
    LOSE = "LOSE"

    def __init__(self):
        """

        """
        self.__state = Game.UNFINISHED

    def get_state(self):
        """
        Returns the Game state: UNFINISHED, WIN, or LOSE
        """
        return self.__state


class Character:
    """
    Character
    """

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        """
        Returns the Character id
        """
        return self.__id

    def get_name(self):
        """
        Returns the Character name
        """
        return self.__name

    def set_name(self, name):
        """
        Changes the Character name
        """
        self.__name = name

    def make_move(self, selection):
        """
        To be implemented
        """
        raise NotImplementedError


class NotValidMoveError(Exception):
    pass

