class games:
    def __init__(self):
        self.totalg = 0
        self.gc = 0
    def rangein(self):
        mn = int(input("Enter the minimum value of the range: "))
        mx = int(input("Enter the maximum value of the range: "))
        pt= mn, mx
        return pt
    def genrandomnum(self, mn, mx):
        randomstr = input("Enter a random string: ")
        num = mn + (id(randomstr) % (mx - mn + 1))
        return num
    def guess(self, mn, mx, num):
        guesslist = []
        for gc in range(1, 6):
            guess = int(input(f"Guess (between {mn} and {mx}): "))
            if guess == num:
                print(f'NICE!!!!! You guessed the number correctly in {gc} guesses.')
                return gc
            elif guess > num:
                print('Guess lower than that!')
            elif guess < num:
                print('Guess higher than that!')
            guesslist.append(guess)
            print(f'Previous Guesses: {guesslist}')
        print(f'BUMMER!!!! The number was {num}.')
        return 5
    def play(self):
        print("Welcome to the number guessing game! You have 5 chances.")
        mn, mx = self.rangein()
        num = self.genrandomnum(mn, mx)
        return self.guess(mn, mx, num)
    def play_again(self):
        self.gc += 1
        self.totalg += self.play()
        avg = self.totalg / self.gc
        print(f"Average number of guesses to guess the correct number: {avg:.2f}")
        while input("Do you want to play again? (yes/no): ").strip().lower() == "yes":
            self.gc += 1
            self.totalg += self.play()
            avg = self.totalg / self.gc
            print(f"Average guesses: {avg:.2f}")
        print(f"Thanks for playing! You played {self.gc} game(s) with an average of {avg:.2f} guesses.")
game = games()
game.play_again()
