import time


class Tutorial:
    def __init__(self):
        self._username = "admin"
        self._password = "12456adm"

    def slice_website(self, website, x, y):
        slicer = slice(x, y)
        return website[slicer]

    def adm_login(self, username, password):
        if self._username == username and self._password == password:
            return True
        else:
            return False

    def set_timer(self, time_limit, break_point=0):
        for x in range(time_limit, break_point, -1):
            print(x)
            time.sleep(1)


# [19.03.22]: Get the [x:y] indexes of the word in text
def find_word(text, word):
    text, word = text.lower(), word.lower()
    idx = text.find(word)
    return f'{idx}:{idx+len(word)-1}'


# [19.03.22]: Get the number of words and their positions in text
def find_count_words(text, word, separator=' '):
    text_list = text.split(separator)
    indexes = []
    while word in text_list:
        indexes.append(text_list.index(word))
        for idx in indexes:
            text_list[idx] = ''
    return text.count(word), indexes


# [19.03.22]: Find and convert all integers and floats into separate list
#             ignoring strings, containing letters
def if_digit(strings):
    purified = []
    for i in strings:
        if type(i) == str:
            if i.isdigit():
                purified.append(int(i))
            elif i.__contains__('.'):
                purified.append(float(i))
            else:
                continue
        elif type(i) == int or type(i) == float:
            purified.append(i)
        else:
            continue
    return purified
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
