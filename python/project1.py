print("hi, welcome to the number guessing game! \nyou have 5 chances to guess the number.")

mnv = int(input("enter the minimum value of the range: "))
mxv = int(input("enter the maximum value of the range: "))
y=object()
x = id(y)
num = mnv + (x % (mxv - mnv + 1))
chances = 5
gc = 0
while gc < chances:
    gc += 1
    guess = int(input(f"please enter your guess (between {mnv} and {mxv}): "))
    if guess == num:
        print('correct! you guessed the number correctly within 5 guesses')
        break
    elif guess > num:
        print('guess is too high.')
    elif guess < num:
        print('guess is too low.')
    elif gc == chances:
        print(f'sorry! you failed, the number was {num}.')