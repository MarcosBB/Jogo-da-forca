import random
WORDS = [
    "cachorro", "gato", "elefante", "tigre", "girafa", "leao", "urso", "zebra", "rinoceronte", "hipopotamo",
    "coelho", "raposa", "lobo", "jaguatirica", "panda", "gorila", "macaco", "orangotango", "canguru", "tamandua",
    "peixe", "golfinho", "baleia", "tubarao", "polvo", "lagosta", "caranguejo", "siri", "ostra", "molusco",
    "passaro", "aguia", "falcao", "coruja", "pato", "galinha", "pavao", "flamingo", "tucano", "pinguim",
    "cavalo", "vaca", "ovelha", "cabrito", "burro", "camelo", "dromedario", "javali", "porco", "bode"
]

class Game:
    def __init__(self):
        self.word = self.random_word()
        self.hidden_word = "_" * len(self.word)

    def random_word(self):
        return random.choice(WORDS)

    def update_hidden_word(self, guess_letter):
        word = ""
        index = 0
        
        for letter in self.word:
            if guess_letter == self.word[index]:
                word += letter
            else:
                word += self.hidden_word[index]
            index += 1
        self.hidden_word = word
    
    def check_win(self):
        return self.hidden_word == self.word
    
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.word:
            self.update_hidden_word(letter)


game = Game()
while True:
    print(game.hidden_word)
    if game.check_win():
        print("You win!")
        break
    letter = input("Enter a letter: ")
    game.guess(letter)