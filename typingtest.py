import csv
import random as r
import time


class Typing:
    '''This class will calculate the WPM of the user.

    Attributes
    ----------
    wrong_words : int
    This will count the wrong words of the user.
    elapsed_time : float
    This will count the elapsed time of the user.
    wpm : int
    This will count the WPM of the user.
    correct_word : list
    This will store the correct words of the user.
    correct_char : list
    This will store the correct characters of the user.
    list_speed : list
    This will store the WPM of the user.
    acc : float
    This will store the accuracy of the user.
    '''
    def __init__(self):
        self.wrong_words = 0
        self.elapsed_time = 0
        self.wpm = 0
        self.correct_word = []
        self.correct_char = []
        self.list_speed = []
        self.acc = 0
            
    def WPM(self, sentence):
        '''This function will calculate the WPM of the user. 
        It will also return the correct words and the correct characters. 
        
        Parameters
        ----------
        sentence : str
            The sentence that the user will type.
        ''' 

        self.reset()
        word_of_st = sentence.split(' ')# this will split the sentence into words
        print(sentence)
        start_time = time.time() # this will start the timer
        typed_sentence = input().split(' ') # this will split the user input into words
        end_time = time.time() # this will end the timer
        dct = {}
    
        # this will check if the user typed the same amount of words as the sentence
        if len(word_of_st) > len(typed_sentence): # if the user typed less words than the sentence
            for i in range(len(word_of_st)):
                try:
                    dct[word_of_st[i]] = typed_sentence[i]
                except:
                    dct[word_of_st[i]] = 'err1' # this will be the error code
        elif len(word_of_st) < len(typed_sentence): # if the user typed more words than the sentence
            for i in range(len(typed_sentence)):
                try:
                    dct[word_of_st[i]] = typed_sentence[i]
                except:
                    dct[typed_sentence[i]] = typed_sentence[i]+'er1' # this will be the error code
        else: # if the user typed the same amount of words as the sentence
            for correctword, typedword in zip(word_of_st,typed_sentence):
                # this will zip the words together and put it in a dictionary
                dct[correctword] = typedword

        # this will check if the user typed the correct words and characters
        for correct, typed in dct.items():
            if correct == typed: # if the user typed the correct word
                self.correct_word.append(typed)
            elif correct != typed: # if the user typed the wrong word
                self.wrong_words += 1
        

            if len(typed) == len(correct): # if the user typed the same amount of characters as the sentence
                for i in range(len(typed)):
                    if typed[i] == correct[i]:
                        self.correct_char.append(typed[i])
            elif len(typed) > len(correct): # if the user typed more characters than the sentence
                for i in range(len(typed)):
                    try:
                        if typed[i] == correct[i]:
                            self.correct_char.append(typed[i])
                    except IndexError: 
                        pass
            elif len(typed) < len(correct): # if the user typed less characters than the sentence
                for i in range(len(correct)): 
                    try: 
                        if typed[i] == correct[i]: 
                            self.correct_char.append(typed[i]) 
                    except IndexError: 
                        pass

        # this will calculate the elapsed time in minutes
        self.elapsed_time = (end_time - start_time) / 60
        # this will calculate the amount of characters the user typed correctly
        self.chars_count = sum(len(word) for word in self.correct_word)
        words_count = self.chars_count / 5  # 5 is average word length
        # this will calculate the WPM
        self.wpm = round(words_count / self.elapsed_time)

        total_char = sum(len(word) for word in typed_sentence)
        # this will calculate the total amount of characters the user typed
        self.acc = (len(self.correct_char) / total_char)*100
        # this will calculate the accuracy of the user

    
        return self.wpm, self.wrong_words, self.acc

    def reset(self):
        self.wrong_words = 0
        self.elapsed_time = 0
        self.wpm = 0
        self.correct_word = []
        self.correct_char = []
        self.list_speed = []
        self.acc = 0

    @property
    def wpm(self):
        return self.__wpm

    @wpm.setter
    def wpm(self, new_):
        self.__wpm = new_

    @property
    def words_typed(self):
        return self.__words_typed

    @words_typed.setter
    def words_typed(self, new_):
        self.__words_typed = new_


    
    
    