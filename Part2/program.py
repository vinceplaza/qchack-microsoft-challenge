# -*- coding: utf-8 -*-
"""
Team Cluedo
Created April 10, 2021
"""
#*********************************** PREWORK **********************************
import os

# Set the run mode for the level of required logging ("prod","debug","trace")

# Set working directory for the program. 
_wd_path = "E:\Projects\Quantum\qchack-microsoft-challenge\Part2"

# Set the working directory to the path set by the user.
try:
    os.chdir(_wd_path)
    print("Working directory changed to:\n    " + _wd_path)
except:
    print("Working directory could not be changed to:\n    " + _wd_path)

#*********************************** PROGRAM **********************************
import numpy as np
import matplotlib.pyplot as plt
from game import Game
from manor import Manor

# The phone rang, startling the two famous dectives, Classical Carl and Quantum Quinn. It was a call from 
# the manor informing them that a terrible crime was committed. A guest was murdered during last night's
# full moon. The other guests were hoping the detectives could come and solve the crime. The detectives
# dropped everything and traveled to the scene of the crime. 

_game = Game()

print("\nThe manor has the following rooms:\n    " + str(_game.Manor().Rooms()))

print("\nThe following guests are suspects:\n    " + str(_game.Manor().Guests()))

print("\nThe the following weapons were found:\n    " + str(_game.Manor().Weapons()))

print("\nThe crime committed (it's a secret!):\n    " + _game.CommitCrime() + "\n")

# When they arrived, the detectives determin that each of the remaining guests knows something about the 
# crime. Each guest knows a room, a person, and a weapon that were not part of the crime. If the detectives 
# interview the guests they will be able to collect the clues to determine, by process of elimination
# which person was the victim, which rooom the crime occurred in, and which weapon was used. The detectives
# also find out that they can only randomly query the guests and ask one question each time. Being competitive,
# they decide on a friendly wager. The detective that correctly determines the details of the crime first 
# is Chief Detective for the day. Carl feels that his tried and true method of methodically asking questions 
# until clues are complete will be the quickest so goes first. He desicdes to build a table and ask questions
# that flip values to true that he flips to false when he discovers they were not part of the crime.

_carlsPerformance = []

for x in range(0, 1000):
    _carlsTable = np.matrix([[True, True, True, True],[True, True, True, True],[True, True, True, True]])
    _carlsIterations = 0

    while np.sum(_carlsTable) > 3 and _carlsIterations < 1000:
        _carlsIterations += 1
        _thisClue = _game.InterrogateGuest()
        _carlsTable[_thisClue[0], _thisClue[1]]=False

    _solved = _game.SubmitGuess(_carlsTable)

    # if _solved:
    #     print("Carl solved the crime after " + str(_carlsIterations) + " interrogations")
    # else:
    #     print("Carl failed to solve the crime")
    
    _carlsPerformance.append(_carlsIterations)

plt.hist(_carlsPerformance, bins=10)
plt.show()

