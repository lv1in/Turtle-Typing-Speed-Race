import time
import turtle
import turtle as turt
from turtle import *



class Type:
    def __init__(self):
        self.start_time = time.time()
        self.words_typed = 0
        self.wrong_words = 0
        self.wpm = 0
    
    def WPM(self, sentence):
        time_passed = (time.time() - self.start_time) / 60
        typing_list = ws.textinput("Python guides", sentence).split(' ')
        for counter, char in enumerate(typing_list):
            correctword = sentence.split(' ')[counter]
            if char == correctword:
                self.words_typed +=1
            else:
                self.wrong_words += 1
        self.wpm = (len(typing_list) + self.words_typed - self.wrong_words) // time_passed
   
    
    @property
    def wpm(self):
        return self.__wpm
    
    @wpm.setter
    def wpm(self, new):
        self.__wpm = new
    
    @property
    def words_typed(self):
        return self.__words_typed
    
    @words_typed.setter
    def words_typed(self, new):
        self.__words_typed = new