

class Players:
    ''''''

    def __init__(self, name: str, turtle_color: str, db): 
        ''' Initialize player class  
        :param name: name of player
        :param turtle_color: color of turtle
        :param db: database
        '''

        self.speed = 0 # this is the speed of the turtle
        self.__name = name # this is the name of the player
        self.turtle_color = turtle_color # this is the color of the turtle
        self.db = db # this is the database
        self.players = {} # this is the dictionary of players
        db.insert(self) # insert new player into databas
    
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
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed



