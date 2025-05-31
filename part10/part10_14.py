import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word)    :   return 1
        elif len(player1_word) < len(player2_word)  :   return 2

class MostVowels (WordGame) :

    def __init__(self, rounds: int):
        super().__init__(rounds)

    def __count_vowels (self, string: str) :
        count = 0
        for char in string :
            if char in "aeiouAEIOU" :
                count += 1
        
        return count

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        count_vow_1 = self.__count_vowels(player1_word)
        count_vow_2 = self.__count_vowels(player2_word)        

        if count_vow_1 > count_vow_2    :   return 1
        elif count_vow_1 < count_vow_2    :   return 2


p = MostVowels(3)
p.play()