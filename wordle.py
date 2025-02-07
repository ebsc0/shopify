# wordle
# 4 letter with 5 guesses
# 4 commits
    # datastructure
    # user interface
    # validation user data
    # testing


# randomly select word
# take in guess word and see if match
import random

class Wordle:
    def __init__(self):
        self.words = ["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]
        self.word = self.word_random()
    
    def word_random(self):
        # generate some num i less than length of words
        i = random.randint(0, len(self.words)-1)
        return self.words[i]

    def word_verify(self, guess):
        if guess == self.word: return True
        else: return False


if __name__ == "__main__":
    wordle = Wordle()
    word = wordle.word

    assert wordle.word_verify(word) == True
    assert wordle.word_verify("test") == True
