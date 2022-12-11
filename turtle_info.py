
class TurtlePlayer: # this class will create a turtle player
    ''' This class will create a turtle player'''
    
    def __init__(self, *players):
        self.turtle_players = []
        for player in players:
            self.turtle_players.append(player)

    def show_players(self):
        for player in self.turtle_players:
            print(player)
    
    def get_players(self):
        return self.turtle_players
    
    def get_player(self, index):
        return self.turtle_players[index]
    
    def get_player_name(self, index):
        return self.turtle_players[index].name
    
    def get_player_color(self, index):
        return self.turtle_players[index].turtle_color
    
    def get_player_speed(self, index):
        return self.turtle_players[index].speed
    
    







    