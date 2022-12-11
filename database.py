import json


class DataBase:

    def insert(self, player): # insert new player
        ''' Insert new player into database file players.json
        >>> insert(turtle_player)
        '''

        new_data = {
            player.name: {
            'color': player.turtle_color,
            'speed': 0
            }
        }
        try: # check if file exist
            with open('players.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError or ValueError: # if file not exist, create new file
            with open('players.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data) # if file exist, update data
            with open('players.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

    def info_reset(self): # reset all player info
        ''' Reset all player info in database file players.json 
        to default value 0 
        >>> info_reset()
        Exiting.......
        >>> info_reset()
        No data file found
        '''
    
        try:
            with open('players.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('No data file found')
        else:
            data_dict.clear()
            with open('players.json', 'w') as data_file:
                json.dump(data_dict, data_file, indent=4)
                print('Exiting.......')

    def update_speed(self, name, speed): # update speed of player
        ''' Update speed of player in database file players.json 
        >>> update_speed(name, speed)
        >>> update_speed('player1', 10)
        >>> update_speed('player2', 20)
        '''

        try:
            with open('players.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('No data file found')
        else:
            data_dict[name]['speed'] = speed
            with open('players.json', 'w') as data_file:
                json.dump(data_dict, data_file, indent=4)

    def data(self):
        ''' Return all data in database file players.json 
        >>> data()
        {'player1': {'color': 'red', 'speed': 10}, 
        'player2': {'color': 'blue', 'speed': 20}}
        '''

        try:
            with open('players.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('No data file found')
        else:
            return data_dict