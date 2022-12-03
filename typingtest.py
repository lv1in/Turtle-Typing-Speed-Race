import time 


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
        self.list_speed = []
        self.acc = 0

    def WPM(self, sentence):
        word_of_st = sentence.split(' ')
        self.correct_char = []
        self.correct_word = []
        start_time = time.time()
        while True:
            print(sentence)
            typing_text = input().split(' ')
            if len(typing_text) == len(word_of_st):
                break
        for counter, word in enumerate(typing_text):
            correctword = word_of_st[counter]
            if word == correctword:
                self.correct_word.append(word)
            else:
                self.wrong_words += 1

            for i in range(len(word_of_st[counter])):
                if word_of_st[counter][i] == typing_text[counter][i]:
                    self.correct_char.append(word[i])

        end_time = time.time()

        self.elapsed_time = (end_time-start_time) / 60
        self.chars_count = sum(len(word) for word in self.correct_word)
        self.words_count = self.chars_count / 5
        self.wpm = round(self.words_count / self.elapsed_time)

        self.total_char = sum(len(word) for word in typing_text)
        self.acc = len(self.correct_char)/self.total_char

        print(f'WPM: {self.wpm}')
        print(f'ERROR: {self.wrong_words}')
        print(f'ACC: {self.acc*100:.2f} %')

        return self.wpm

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

    def add_speed(self, speed):
        self.list_speed.append(speed)