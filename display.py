import os
import time
import turtle
from turtle import *

from turtle_info import TurtlePlayer


class Display:
    def __init__(self, db):
        self.dict_ = {}
        self.db = db

    def intro(self):
        '''This function will display the intro screen.'''
        print("===========================================")
        print('   WELCOME TO TURTLE TYPING SPEED RACE     ')
        print("===========================================")
        print('1. Single Player')
        print('2. MultiPlayer')
        print("===========================================")


    def single_mode(self):
        '''This function will display the single player mode.'''
        os.system('clear')
        print("===========================================")
        print('           MODE SINGLE PLAYER              ')
        print("===========================================")


    def multiplayer(self):
        '''This function will display the multiplayer mode.'''
        os.system('clear')
        print("===========================================")
        print('           MODE MULTIPLAYER                ')
        print('===========================================')


    def single_lv(self):
        '''This function will display the single player level.'''
        os.system('clear')
        name = input(f'Player Name: ')
        color = input(f'Player Color: ')
        
        return name, color

    def multi(self):
        os.system('clear')
        name = input(f'Player Name: ')
        color = input(f'Player Color: ')
        return name, color


    def turtle_display(self, amount):
        '''This function will display the turtle screen.
        amount: 1 for single player, more than 2 for multiplayer.'''

        data_dict = self.db.data()
        lst_name = [name for name in data_dict.keys()]
        t = turtle.Turtle()
        scr = Screen()
        # SCREEN SETUP

        scr.setup(800, 500)
        scr.title("Track")
        scr.bgcolor("White")
        t.speed(0)
        # HEADING
        t.penup()
        t.goto(-100, 205)
        t.color("black")
        t.write("Turtle Racing", font=("Arial", 20, "bold"))
        # DIRT
        t.goto(-350, 200)
        t.pendown()
        t.color("blue")
        t.begin_fill()
        for i in range(2):
            t.forward(700)
            t.right(90)
            t.forward(400)
            t.right(90)
        t.end_fill()

        # FINISH LINE
        gap_size = 20
        t.shape("square")
        t.penup()

        t.color("white")
        for i in range(10):
            # WHITE SQUARES ROW 1
            t.goto(250, (170 - (i * gap_size * 2)))
            t.stamp()
            # WHITE SQUARES ROW 2
            t.goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
            t.stamp()
        t.color("black")
        for i in range(10):
            # BLACK SQUARES ROW 1
            t.goto(250, (190 - (i * gap_size * 2)))
            t.stamp()
            # BLACK SQUARES ROW 2
            t.goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
            t.stamp()
        if amount == 1: # single player
            scr = turtle.Screen()
            scr.tracer(0)

            player_1 = turtle.Turtle() # player
            timer_text = turtle.Turtle() # timer
            # first player details
            player_1.color(data_dict[lst_name[0]]['color'])
            player_1.shape('turtle')

            # first player proceeds to racing track
            player_1.penup()
            player_1.goto(-300, 0)
            player_1.pendown()

            start = time.time()
            while player_1.xcor() <= 230:
                player_1.forward(data_dict[lst_name[0]]['speed'])
                
                timer_text.clear()
                timer_text.write(int(time.time() - start), font=("Courier", 30))
                scr.update()
             

        elif amount == 2: # multiplayer
            scr = turtle.Screen()
            scr.tracer(0)

            player_1 = turtle.Turtle()
            timer_text = turtle.Turtle()
            # first player details
            player_1.color(data_dict[lst_name[0]]['color'])
            player_1.shape('turtle')

            # first player proceeds to racing track
            player_1.penup()
            player_1.goto(-300, 100)
            player_1.pendown()
            # second player details
            player_2 = turtle.Turtle()
            # second player proceeds to racing track
            player_2.color(data_dict[lst_name[1]]['color'])
            player_2.shape('turtle')

            # second player proceeds to racing track
            player_2.penup()
            player_2.goto(-300, 0)
            player_2.pendown()

            start = time.time()
            while player_1.xcor() <= 230 and player_2.xcor() <= 230:
                player_1.forward(data_dict[lst_name[0]]['speed'])
                player_2.forward(data_dict[lst_name[1]]['speed'])
                timer_text.clear()
                timer_text.write(int(time.time() - start), font=("Courier", 30))
                scr.update()
            if player_1.xcor() > player_2.xcor():
                os.system('clear')
                print(f'{lst_name[0]} WIN!!!!')
            elif player_2.xcor() > player_1.xcor():
                os.system('clear')
                print(f'{lst_name[1]} WIN!!!!')
            turtle.done()

        elif amount == 3: # multiplayer
            scr = turtle.Screen()
            scr.tracer(0)

            player_1 = turtle.Turtle()
            timer_text = turtle.Turtle()
            # first player details
            player_1.color(data_dict[lst_name[0]]['color'])
            player_1.shape('turtle')

            # first player proceeds to racing track
            player_1.penup()
            player_1.goto(-300, 200)
            player_1.pendown()
            # second player details
            player_2 = turtle.Turtle()
        
            player_2.color(data_dict[lst_name[1]]['color'])# second player proceeds to racing track
            player_2.shape('turtle')

          
            player_2.penup() # second player proceeds to racing track
            player_2.goto(-300, 100)
            player_2.pendown()


            player_3 = turtle.Turtle()
            timer_text = turtle.Turtle()
   
            player_3.color(data_dict[lst_name[2]]['color']) 
            player_3.shape('turtle')

            
            player_3.penup() 
            player_3.goto(-300, 0)
            player_3.pendown()

            start = time.time()
            while player_1.xcor() <= 230 and player_2.xcor() <= 230 and player_3.xcor() <= 230:
                player_1.forward(data_dict[lst_name[0]]['speed'])
                player_2.forward(data_dict[lst_name[1]]['speed'])
                player_3.forward(data_dict[lst_name[2]]['speed'])
                timer_text.clear()
                timer_text.write(int(time.time() - start), font=("Courier", 30))
                scr.update()
            if player_1.xcor() > player_2.xcor() and player_1.xcor() > player_3.xcor():
                os.system('clear')
                print(f'{lst_name[0]} WIN!!!!')
            elif player_2.xcor() > player_1.xcor() and player_2.xcor() > player_3.xcor:
                os.system('clear')
                print(f'{lst_name[1]} WIN!!!!')
            elif player_3.xcor() > player_1.xcor() and player_3.xcor() > player_2.xcor():
                os.system('clear')
                print(f'{lst_name[2]} WIN!!!!')
            turtle.done()
        elif amount == 4: # multiplayer
            scr = turtle.Screen()
            scr.tracer(0)

            player_1 = turtle.Turtle()
            timer_text = turtle.Turtle()
            # first player details
            player_1.color(data_dict[lst_name[0]]['color'])
            player_1.shape('turtle')

            # first player proceeds to racing track
            player_1.penup()
            player_1.goto(-300, 200)
            player_1.pendown()

            player_2 = turtle.Turtle()
            
            player_2.color(data_dict[lst_name[1]]['color'])
            player_2.shape('turtle')

         
            player_2.penup()
            player_2.goto(-300, 100)
            player_2.pendown()


            player_3 = turtle.Turtle()
            timer_text = turtle.Turtle()
            
            player_3.color(data_dict[lst_name[2]]['color'])
            player_3.shape('turtle')

           
            player_3.penup()
            player_3.goto(-300, 0)
            player_3.pendown()

            player_4 = turtle.Turtle()
            timer_text = turtle.Turtle()
           
            player_4.color(data_dict[lst_name[3]]['color'])
            player_4.shape('turtle')


            player_4.penup()
            player_4.goto(-300, -100)
            player_4.pendown()

            start = time.time()
            while player_1.xcor() <= 230 and player_2.xcor() <= 230 and \
                    player_3.xcor() <= 230 and player_4.xcor() <= 230:
                player_1.forward(data_dict[lst_name[0]]['speed'])
                player_2.forward(data_dict[lst_name[1]]['speed'])
                player_3.forward(data_dict[lst_name[2]]['speed'])
                player_4.forward(data_dict[lst_name[3]]['speed'])
                timer_text.clear()
                timer_text.write(int(time.time() - start), font=("Courier", 30))
                scr.update()
            if player_1.xcor() > player_2.xcor() and player_1.xcor() >\
                    player_3.xcor() and player_1.xcor() > player_4.xcor():
                os.system('clear')
                print(f'{lst_name[0]} WIN!!!!')
            elif player_2.xcor() > player_1.xcor() and player_2.xcor() > \
                    player_3.xcor() and player_2.xcor() > player_4.xcor():
                os.system('clear')
                print(f'{lst_name[1]} WIN!!!!')
            elif player_3.xcor() > player_1.xcor() and player_3.xcor() > \
                    player_2.xcor() and player_3.xcor() > player_4.xcor():
                os.system('clear')
                print(f'{lst_name[2]} WIN!!!!')
            elif player_4.xcor() > player_1.xcor() and player_4.xcor() > \
                    player_2.xcor() and player_4.xcor() > player_3.xcor():
                os.system('clear')
                print(f'{lst_name[3]} WIN!!!!')
            turtle.done()
