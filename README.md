# Project: Turtle Typing Speed Race  
## Project overview:
---
###  Create games for typing practice or for typing competitions with others. The typing speed (WPM) is used to calculate the distance forward of the turtle.  

## Features
---
* The program has a menu to choose single player and multiplayer modes(multiplayer mode Up to 4 players).  
* The program calculate wpm typing speed  
* The program set color and distance forward of the turtle  
* The program show turtle racing 

## Required libraries and tools
---
* python3.6 or more than
* os module
* time module
* random module
* json module
* csv module
## Program design & Code structure

---
* database.py (class DataBase)  
    This class stores the player's data as a json file. and manage information
* display.py (class Display)  
This class shows all windows of program execution. including turtle graphics
* player.py (class Players)  
    This class will initialize player info
* typingtest.py (class Typing)  
This class will calculate the WPM of the user  
* turtle_info.py (class TurtlePlayer)  
This class is used to store information about the turtle player and the database information about the player in the database file players.json  
* sentences.csv  
This file stores sentences to be typed accordingly.
* main.py  
This file is for running the program.


## How to run
---
To run the program, you can use the command below in the terminal  
First, you need to clone the repository to your local machine: 
```py
% cd filelocation 
% git clone https://github.com/lv1in/Turtle-Typing-Speed-Race.git
% python3 main.py 
```
if it doesn't work, try this command
```py
% python3.10 main.py
```  

## How to play
---
* choese mode.
* single player : enter your info.  
multiplayer mode : enter num of player.
* single player : start type  
multiplayer mode : Enter player information and then start typing starting with the first person and working your way up to the last person. 
* After finishing typing, the program will show wpm, error word and acc.
* Then the turtle graphics window will show the turtle race.

### Github of the Project
---
```py
https://github.com/lv1in/Turtle-Typing-Speed-Race
```






