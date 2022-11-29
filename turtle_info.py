class Turtle:

    def __init__(self, name: str, turtle_color: str, db, typ):
        self.name = name
        self.turtle_color = turtle_color
        self.db = db
        self.typ = typ
        db.insert(self)
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

    def turtle_speed(self, list_speed, name):
        self.db.set_speed(list_speed, name)

    def turtle_win(self):
        pass

    pass
    