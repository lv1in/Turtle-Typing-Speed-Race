import time 
import turtle as t

class Typing:

    def __init__(self):
        self.words_typed = 0
        self.wrong_words = 0
        self.words_count = 0
        self.chars_count = 0
        self.elapsed_time = 0
        self.wpm = 0
        self.correct_word = []
        self.correct_char = []
        self.total_char = 0
        self.wrong_char = 0


    def WPM(self, sentence):
        word_of_st = sentence.split(' ')
        self.start_time = time.time()
        while True:
            print(sentence)
            self.text = input().split(' ')
            if len(self.text) == len(word_of_st) :
                break
        for counter, word in enumerate(self.text):
            correctword = word_of_st[counter]
            self.total_char += len(word_of_st[counter])
            if word == correctword:
                self.words_typed += 1
                self.correct_word.append(word)
            else:
                self.wrong_words += 1

            for i in range(len(self.text[counter])):
                correctchar = word_of_st[counter][i]
                if word[i] == correctchar:
                    self.correct_char.append(word[i])
    

        self.end_time = time.time()

        self.elapsed_time = (self.end_time-self.start_time) / 60
        self.chars_count = sum(len(word) for word in self.correct_word)
        self.words_count = self.chars_count / 5
        self.wpm = round(self.words_count/ self.elapsed_time)

        self.acc = len(self.correct_char)/self.total_char
        print(f'WPM: {self.wpm}')
        print(f'ERROR: {self.wrong_words}')
        print(f'ACC: {self.acc*100} %')

        return self.wpm

        # time_passed = (time.time() - self.start_time) / 60
        # typing_list = ws.textinput("Python guides", sentence).split(' ')
        # for counter, char in enumerate(typing_list):
        #     correctword = sentence.split(' ')[counter]
        #     if char == correctword:
        #         self.words_typed +=1
        #     else:
        #         self.wrong_words += 1
        # self.wpm = (len(typing_list) + self.words_typed - self.wrong_words) // time_passed
        
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