# -*- coding: utf-8 -*-
"""
Team Cluedo
Created April 10, 2021
"""
# import types
# from logger import Logger
# from vectorizer import Vectorizer
# from model_runner import ModelRunner


class Manor:
    '''
    Manages the gameplay
    
    Args:
        debug: bool: If true, conditionally executes debug code. 
        logger: logger.Logger: Responsible for logging tasks. 
    '''

    
    def __init__(self):#, x, class_labels, run_mode, logger=None):
        '''Initialization tasks for the class.
        '''
        _name = "Game.Initializer"
        self._rooms = ["Billiard Room","Conservatory","Study","Kitchen"]
        self._guests = ["Colonel Mustard","Professor Plum","Mrs. Peacock","Miss Scarlet"]
        self._weapons = ["Candlstick", "Rope", "Wrench", "Knife"]

    def Rooms(self):
        return self._rooms
    

    def Guests(self):
        return self._guests
    

    def Weapons(self):
        return self._weapons
      