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
msg = 'S T A R T I N G . . . 3 2 1'
with open('sentences.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        st.append(row)

while True:
    display.intro()
    choice = input('Choose the mode (or [exit] to quit): ')
    if choice == 'exit':
        break
    elif choice == '1':
        display.single_mode()
        level = input('Enter [1] to continue (or [back]): ')
        if level == 'back':
            os.system('clear')
            continue
        else:
            indexx = randint(0, len(st))
            sentence = st[indexx][0]
            for i in range(int(level)):
                name, color = display.single_lv()
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
            display.turtle_display(1)
            time.sleep(1)
            input('Press [enter] to exit')
            time.sleep(1)
            db.info_reset()
    

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
            time.sleep(1)
            db.info_reset()

