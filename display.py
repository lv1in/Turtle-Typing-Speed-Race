from turtle import *
import turtle
import time
from turtle_info import TurtlePlayer
import os

class Display(TurtlePlayer):

    def __int__(self, db):
        self.db = db
        db.insert(self)
        pass

    def intro(self):
        print("===========================================")
        print('   WELCOME TO TURTLE TYPING SPEED RACE     ')
        print("===========================================")
        print('1. Single Player')
        print('2. MultiPlayer')
        print("===========================================")
        while True:
            try:
                mode = int(input('Choese mode(1/2): '))
            except:
                print("Please Enter Integers 1-2")
            else:
                if mode == 1 or mode == 2:
                    break
        return mode

    def single_mode(self):
        os.system('clear')
        print("===========================================")
        print('           MODE SINGLE PLAYER              ')
        print("===========================================")
        print('1. Level(1)')
        print('2. Level(2)')
        print('3. Level(3)')
        print('4. back')
        print("===========================================")
        while True:
            try:
                lv = int(input('Choese level(1/2/3/4): '))
            except:
                print("Please Enter an Integer 1-4 ")
            else:
                if lv in [1, 2, 3, 4]:
                    if lv == 4:
                        os.system('clear')
                        mode_ = self.intro()
                        if mode_ == 1:
                            self.single_mode()
                        else:
                            self.multiplayer()
                    else:
                        return lv

    def multiplayer(self):
        print("===========================================")
        print('           MODE MULTIPLAYER                ')
        print("===========================================")
        print('1. Enter amount player')
        print('2. Back')
        print('===========================================')
        while True:
            try:
                choice = int(input('Enter(1/2): '))
            except:
                print("Please Enter an Integer 1-2 ")
            else:
                if choice in [1, 2]:
                    if choice == 2:
                        os.system('clear')
                        mode_ = self.intro()
                        if mode_ == 2:
                            self.multiplayer()
                        else:
                            self.single_mode()
                    else:
                        num = int(input('Enter num of Player: '))

                        return num

    def single_lv(self, lv):
        if lv == 1:
            pass
        elif lv == 2:
            pass
        elif lv == 3:
            pass



    def multi(self, num):
        for i in range(num):
            name = input(f'Player{i + 1} Name: ')
            PlayerName.append(name)
            color = input(f'Player{i + 1} Color: ')
            TurtlePlayer(name, color, self.db)


    def saving(self):
        pass

    def play_again(self):
        pass










    def turtle_display(self):
        # SCREEN SETUP
        setup(800, 500)
        title("Track")
        bgcolor("White")
        speed(0)
        # HEADING
        penup()
        goto(-100, 205)
        color("black")
        write("PAT <3 PIMPLOY", font=("Arial", 20, "bold"))
        # DIRT
        goto(-350, 200)
        pendown()
        color("blue")
        begin_fill()

        for i in range(2):
            forward(700)
            right(90)
            forward(400)
            right(90)
        end_fill()

        # FINISH LINE
        gap_size = 20
        shape("square")
        penup()

        color("white")
        for i in range(10):
            # WHITE SQUARES ROW 1
            goto(250, (170 - (i * gap_size * 2)))
            stamp()
            # WHITE SQUARES ROW 2
            goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
            stamp()
        color("black")
        for i in range(10):
            # BLACK SQUARES ROW 1
            goto(250, (190 - (i * gap_size * 2)))
            stamp()
            # BLACK SQUARES ROW 2
            goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
            stamp()

        turtle.exitonclick()

    def tutle_intrack(self, num, msg, speed):
        super().turtle_track(msg)
        super().turtle_setup(num)
        super().turtle_timer(speed)
        # self.ttplayer.turtle_track(msg)
        # self.ttplayer.turtle_setup(num)
        # self.ttplayer.turtle_timer(speed)

    # def turtle_setup(self, num):
    #     dict_ = self.db.data()
    #     if num == 1:
    #         for single in dict_.values():
    #             self.turt.color(single['color'])
    #             self.turt.shape('turtle')
    #             self.turt.shapesize(2)
    #             self.turt.penup()
    #             self.turt.goto(-300, -0)
    #             self.turt.pendown()
    #     elif num <= 4:
    #         y = 150
    #         for multi in dict_.values():
    #             self.turt.color(multi['color'])
    #             self.turt.shape('turtle')
    #             self.turt.shapesize(2)
    #             self.turt.penup()
    #             self.turt.goto(-300, y)
    #             self.turt.pendown()
    #             y -= 100

    pass


