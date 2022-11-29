import json


class DataBase:

    def insert(self, turtle_player):
        new_data = {
            turtle_player.name: {
            'color': turtle_player.turtle_color,
            'speed': 0
            }
        }
        try:
            with open('players.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('players.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('players.json', 'w') as data_file:
                json.dump(data, data_file, indent=4) 

                
    def info_reset(self):
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


    def set_speed(self, speed, name):
            try:
                with open('players.json', 'r') as data_file:
                    data_dict = json.load(data_file)
            except FileNotFoundError:
                print('No data file found')
            else:
                data_dict[name]['speed'] =  speed
                with open('players.json', 'w') as data_file:
                    json.dump(data_dict, data_file, indent=4)
                            
    def add_player(self, turtle_player):
        try:
            with open('players.json', 'r') as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print('No data file found')
        else:
            data_dict[turtle_player.name] = {'color': turtle_player.turtle_color, 'speed': 0}
            with open('players.json', 'w') as data_file:
                        json.dump(data_dict, data_file, indent=4)
                        print('ADDED Player')
                        