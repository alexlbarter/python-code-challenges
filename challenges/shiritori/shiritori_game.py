class Shiritori:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        valid_word = False
        # Check if word is valid
        if len(self.words) == 0:
            valid_word = True
        elif word not in self.words and self.words[-1][-1] == word[0]:
            valid_word = True

        if valid_word:
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"

