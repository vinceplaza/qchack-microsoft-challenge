# -*- coding: utf-8 -*-
"""
Team Cluedo
Created April 10, 2021
"""
import qsharp
import numpy as np
from manor import Manor
from QuantumSolvers import RandomNumberInRange

class Game:
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
        self._manor = Manor()
        self._guestRow = 0
        self._roomRow = 1
        self._weaponRow = 2 
        self._clueTable = np.matrix([[False, False, False,False],[False, False, False,False],[False, False, False,False]])

    def Manor(self):
        return self._manor

    def CommitCrime(self):
        # Determine the victim
        self._murderer = RandomNumberInRange.simulate(min=0,max=3, avoid=5)
        self._room = RandomNumberInRange.simulate(min=0,max=3, avoid=5)
        self._weapon = RandomNumberInRange.simulate(min=0,max=3, avoid=5)

        self._clueTable[self._guestRow, self._murderer] = True
        self._clueTable[self._roomRow, self._room] = True
        self._clueTable[self._weaponRow, self._weapon] = True

        self._theCrime = "The duke was murdered by " + self._manor.Guests()[self._murderer] + " in the " +  self._manor.Rooms()[self._room] + " with the " + self._manor.Weapons()[self._weapon]              
       
        return(self._theCrime)

    def InterrogateGuest(self):
        _clueIndex = RandomNumberInRange.simulate(min=0,max=8, avoid=9)
        _falseIndices = np.matrix(np.where(self._clueTable == False))
        return [_falseIndices[0, _clueIndex], _falseIndices[1,_clueIndex]]

    def SubmitGuess(self, guess):
        _result = guess == self._clueTable
        if np.sum(_result) == 12:
            return True
        else:
            return False
        
    