import turtle
from database import DataBase
from turtle_info import TurtlePlayer
from display import Display
from typingtest import Typing
import time
import sys , subprocess
import turtle as t
from turtle import Screen, Turtle
import countdown as countdown
from turtle import *
from random import *
import turtle
import time



sentence = 'the quick brown fox jumps over the little lazy dog.'

db = DataBase()
typ = Typing()

mode = Display().intro()
if mode == 1:
    Display().single_mode()
elif mode == 2:
    num = Display().multiplayer()
    for i in range(num):
        name, color = Display().multi()
        TurtlePlayer(name, color, db)
    dict_ = db.data()
    for name in dict_.keys:
        wpm = typ.WPM(sentence)
        typ.add_speed(wpm)
        db.update_speed(name, wpm)
print(typ.list_speed)






















# db = DataBase()
# typ = Typing()
# playerlist = []
# PlayerName = []
# display = Display()
# # display = Display(TurtlePlayer('jack','red', db))
# # msg = 'S T A R T  I N G . . .3 2 1'
# p1 = TurtlePlayer('Meen', 'red', db)
# p1.add_player(0)
# print(p1.players)
# sentence = 'the quick brown fox jumps over the little lazy dog.'


# num = int(input('Amount of player: '))
# for i in range(num):
#     name = input(f'Player{i+1} Name: ')
#     PlayerName.append(name)
#     color = input(f'Player{i+1} Color: ')
#     TurtlePlayer(name, color, db)
# print(PlayerName)
# for py in range(len(PlayerName)):
#     input(' Press enter to START...')
#     for i in range(len(msg)):
#         print(msg[i], end='')
#         time.sleep(0.3)
#     print()
#     wpm = typ.WPM(sentence)
#     db.set_speed(wpm, PlayerName[py])
#     wpm = 0

# dict_ = db.data()
# num = int(input('Amount of player: '))
# for i in range(num):
#     name = input(f'Player{i+1} Name: ')
#     PlayerName.append(name)
#     color = input(f'Player{i+1} Color: ')
#     TurtlePlayer(name, color, db)
# display.tutle_intrack(num, 'RACING', 1)
# py = TurtlePlayer('Nut', 'blue', db)
# py.turtle_track('KUY Vin')
# py.turtle_setup(num)
# py.turtle_timer(0.5)



# py.turtle_detail()




    # time.sleep(0.5)

# time.sleep(0.5)
# msg = 'S T A R T  I N G . . .3 2 1'
# for i in range(len(msg)):
#     print(msg[i],end='')
#     time.sleep(0.3)
# print()



# for name in PlayerName:
#         db.set_speed(wpm, name)


#

# dict = {'nut': {'color': 'red', 'speed': 0}}

# import os
# from time import sleep
#
# # some text
# print("a")
# print("b")
# print("c")
# print("d")
# print("e")
# print("Screen will now be cleared in 5 Seconds")
#
# # Waiting for 5 seconds to clear the screen
# sleep(5)
#
# # Clearing the Screen
# os.system('clear')



