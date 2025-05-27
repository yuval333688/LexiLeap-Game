import pandas as pd
from datetime import date

class Word:
    def __init__(self, word: str):
        self._word = word  # Note: _word with underscore means "private by convention"
        self._date_to_add = date.today()

    def word(self):
        return self._word

    def word(self, new_word):
        if not new_word.isalpha():
            raise ValueError("Word must only contain letters.")
        self._word = new_word

    def date_to_add(self):
        return self._date_to_add

    def __str__(self):
        return f"Word('{self._word}', Date Added: {self._date_to_add})"
    
    def __repr__(self):
        return f"{self._word}"

    def __len__(self):
        return len(self._word)
    
    def init_answer(self):
        self.word = input("Enter a word to be used in the question: ")

    def get_word(self):
        return self._word  # optional if you're using .word already

    def set_word(self, new_word):
        self.word = new_word  # calls the setter logic above
