import turtle as t
from turtle import Screen, Turtle
import countdown as countdown
from turtle import *
from random import *
import turtle
import time


class TurtlePlayer:

    def __init__(self, name: str, turtle_color: str, db):
        self.name = name
        self.turtle_color = turtle_color
        self.db = db
        self.players = {}
        # self.turt = turtle.Turtle()
        # self.scr = turtle.Screen()
        db.insert(self)
        # self.typ = typ
        # typ.insert(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def turtle_color(self):
        return self.__turtle_color
    
    @turtle_color.setter
    def turtle_color(self, new_color):
        self.__turtle_color = new_color

    # def add_player(self):
        # self.players[self.name] = [self.turtle_color]

    # def add_speed(self, speed):
        # for valuese in self.players.values():





    def turtle_track(self, msg):
        # SCREEN SETUP
        setup(800, 500)
        title("Track")
        bgcolor("White")
        speed(0)

        # HEADING
        penup()
        goto(-100, 205)
        color("black")
        write(msg, font=("Arial", 20, "bold"))

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

        # WHITE SQUARES ROW 1
        color("white")
        for i in range(10):
            goto(250, (170 - (i * gap_size * 2)))
            stamp()

        # WHITE SQUARES ROW 2
        for i in range(10):
            goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
            stamp()

        # BLACK SQUARES ROW 1
        color("black")
        for i in range(10):
            goto(250, (190 - (i * gap_size * 2)))
            stamp()

        # BLACK SQUARES ROW 2
        for i in range(10):
            goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
            stamp()

    def turtle_win(self):
        pass


    def countdown(self, time):
        FONT = ('Arial', 30, 'normal')
        screen = Screen()
        screen.onclick(None)  # disable click until countdown completes
        turtle.clear()
        if time > 0:
            turtle.write(time, align='center', font=FONT)
            screen.ontimer(lambda: self.countdown(time - 1), 1000)
        else:
            turtle.write("Click Screen", align='center', font=FONT)
            screen.onclick(lambda x, y: self.countdown(30))

    def turtle_setup(self, num):
        dict_ = self.db.data()
        turt = turtle.Turtle()
        if num == 1:
            for single in dict_.values():
                turt.color(single['color'])
                turt.shape('turtle')
                turt.shapesize(2)
                turt.penup()
                turt.goto(-300, 0)
                turt.pendown()
        elif num <= 4:
            y = 150
            for multi in dict_.values():
                turt.color(multi['color'])
                turt.shape('turtle')
                turt.shapesize(2)
                turt.penup()
                turt.goto(-300, y)
                turt.pendown()
                y -= 100


    def turtle_timer(self, speed):
        turt = turtle.Turtle
        scr = turtle.Screen()
        scr.tracer(0)
        timer_text = turt
        turt.speed(speed)
        start = time.time()
        while turt.xcor() <= 230:
            turt.forward(speed)
            timer_text.clear()
            timer_text.write(int(time.time() - start), font=("Courier", 30))
            scr.update()
        turtle.done()









    