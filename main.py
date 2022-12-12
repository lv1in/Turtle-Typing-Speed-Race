import csv
import os
import time
from random import randint
from time import sleep
from database import DataBase
from display import Display
from player import Players
from typingtest import Typing



db = DataBase()
typ = Typing()
display = Display(db)
st = []
msg = 'S T A R T I N G . . . '
count = '321'
with open('sentences.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        st.append(row)

while True: 
    display.intro() # display intro
    choice = input('Choose the mode (or [exit] to quit): ') # choose the mode
    if choice == 'exit': # if the user choose to exit
        break
    elif choice == '1': # if the user choose single player
        display.single_mode()
        level = input('Enter [1] to continue (or [back]): ') 
        if level == 'back': # if the user choose to go back
            os.system('clear')
            continue
        else:
            indexx = randint(0, len(st)) # this will choose a random sentence
            sentence = st[indexx][0] # this will get the sentence
            for i in range(int(level)):
                name, color = display.single_lv()
                Players(name, color, db)
                for i in msg:
                    sleep(0.1)
                    print(i, end='', flush=True) 
                for i in count:
                    sleep(1)
                    print(i, end='', flush=True) # this will display the countdown
                print()
                wpm, error, acc = typ.WPM(sentence) # this will get the WPM, error, and accuracy
                print(f'WPM: {wpm}')
                print(f'Error: {error}')
                print(f'Accuracy: {acc:.2f}%')
                db.update_speed(name, wpm/100) # this will update the speed of the user
                input('Press [enter] to continue')
            display.turtle_display(1) # this will display the turtle
            time.sleep(1)
            input('Press [enter] to exit')
            db.info_reset()
            time.sleep(1.5)
            os.system('clear')
    

    elif choice == '2':
        display.multiplayer()
        amount = input('Enter amount player[2-4] (or [back]): ')
        if amount == 'back':
            os.system('clear')
            continue
        else:
            indexx = randint(0, len(st))
            sentence = st[indexx][0]
            for i in range(int(amount)):
                name, color = display.multi()
                Players(name, color, db)
                for i in msg:
                    sleep(0.1)
                    print(i, end='', flush=True)
                print()
                wpm, error, acc = typ.WPM(sentence)
                print(f'WPM: {wpm}')
                print(f'Error: {error}')
                print(f'Accuracy: {acc:.2f}%')
                db.update_speed(name, wpm/100)
                input('Press [enter] to continue')
            display.turtle_display(int(amount))
            time.sleep(1)
            input('Press [enter] to exit')
            db.info_reset()
            time.sleep(1)
            os.system('clear')

