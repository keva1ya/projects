def get_movie():
    randomstr = input("Enter a random string: ")
    num = (id(randomstr) % (len([movie_list]))) + 1
    movie_list = ["Dangal", "Queen", "Barfi", "Bajrangi Bhaijaan", "PK", "Gully Boy", "Piku", "Zindagi Na Milegi Dobara", "Kahaani", "Tanu Weds Manu", "Haider", "Article", "Masaan", "Andhadhun", "Badhaai Ho", "Stree", "Raazi", "Paan Singh Tomar", "The Lunchbox", "Chhichhore", "Dear Zindagi", "Tamasha", "Kapoor and Sons", "Bhaag Milkha Bhaag", "Pink", "Neerja", "Talvar", "Shahid", "Mardaani", "Gangs of Wasseypur", "Drishyam", "Badlapur", "Padmaavat", "Sanju", "Sultan", "Kesari", "Manmarziyaan", "October", "Sui Dhaaga", "Sonu Ke Titu Ki Sweety", "Hindi Medium", "Newton", "Mulk", "Bareilly Ki Barfi", "Secret Superstar", "Dum Laga Ke Haisha", "Shubh Mangal Saavdhan", "Toilet Ek Prem Katha", "Airlift", "Rustom", "Raees", "Fan", "Dilwale", "Ae Dil Hai Mushkil", "Udta Punjab", "Sarbjit", "Ki and Ka", "Wazir", "Bajirao Mastani", "Tamasha", "Piku", "Dil Dhadakne Do", "Badlapur", "PK", "Haider", "Queen", "Gunday", "Dhoom", "Chennai Express", "Yeh Jawaani Hai Deewani", "Barfi", "Kahaani", "Zindagi Na Milegi Dobara", "Rockstar", "Delhi Belly", "Don", "Ra One", "Bodyguard", "Singham", "Dabangg", "My Name Is Khan", "Wake Up Sid", "Kaminey", "Dev"]
    index = id(num) % len(movie_list) 
    return movie_list[index].lower()

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    print("Welcome to Movie Guessing Game !")
    word = get_movie()
    guessed_letters = set()
    attempts = 5
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter (only words): ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good job! That letter is in the word.")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                return
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    
    print("\nGame over! The word was:", word)

hangman()
