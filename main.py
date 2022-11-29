from database import DataBase
from turtle_info import TurtlePlayer
# from display import Display
from typingtest import Typing
import time
import turtle as t




db = DataBase()
typ = Typing()
PlayerName = []
sentence = 'the quick brown fox jumps over the little lazy dog.'
num = int(input('Amount of player: '))
for i in range(num):
    name = input(f'Player{i+1} Name: ')
    color = input(f'Player{i+1} Color: ')
    TurtlePlayer(name, color, db)

for py in PlayerName:
    wpm = 0
    wpm = typ.WPM(sentence)
    db.set_speed(wpm, py)



