import turtle

class TurtlePlayer:

    def __init__(self, name: str, turtle_color: str, db):
        self.name = name
        self.turtle_color = turtle_color
        self.db = db
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


    def turtle_racetrack(self):
        pass



    def turtle_win(self):

        pass

    def turtle_detail(self):
        py = turtle.Turtle()
        dict_player = self.db.data()
        for name in dict_player:
            py.color(dict_player[name]['color'])
            py.speed(dict_player[name]['speed'])

    def turtle_setup(self, name):
        y = 150
        for i in range(len(self.db.data())):
            name.shapesize(1.5)
            name.penup()
            name.goto(-300, y)
            name.pendown()
            y -= 100







    