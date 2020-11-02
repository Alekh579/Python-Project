import random

# words to guess from(random words would be chosen from this list)
word_list = ['omen', 'raze', 'phoenix', 'sage', 'brimstone', 'viper',
             'killjoy', 'skye', 'sova', 'cypher', 'reyna', 'breach']

# function to get a random word out of the above list


def get_word():
    word = random.choice(word_list)
    return word.upper()

# function for the main mechanism of the game


def play(word):
    word_completion = "_" * len(word)   # blank for the letters of the random word to be guessed
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("\n__________WELCOME TO HANGMAN , MAKE SURE YOU DIDN'T GET HANGED !__________\n")   # Welcome Note !
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # if tries == 0, game over !
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()   # ignore letter case (not a case sensitive game)
        print("\n")
        # if only 1 letter is guessed
        if len(guess) == 1 and guess.isalpha():

            # if the letter is already guessed and is not in the word then it wont count the try
            if guess in guessed_letters:
                print("***** You already guessed the letter", guess, " *****\n")

            # if the letter is not present in the word then reduce lifeline by 1
            elif guess not in word:
                print("***** ", guess, "is not in the word. *****\n")
                tries -= 1
                guessed_letters.append(guess)

            # if the letter is present fill all the blanks corresponding to that letter
            else:
                print("***** Good job,", guess, "is in the word! *****\n")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # if whole word is guessed
        elif len(guess) == len(word) and guess.isalpha():

            # to keep track of inputed words(i.e not to input the word more than once if its wrong)
            if guess in guessed_words:
                print("***** You already guessed the word", guess, " *****\n")

            # if the guessed word doesnt matches with the actual word
            elif guess != word:
                print("***** ", guess, "is not the word. *****\n")
                tries -= 1
                guessed_words.append(guess)

            #  if the guessed word matches the actual word
            else:
                guessed = True
                word_completion = word

        # if the inputed letter doeesnt match any letter from the word
        else:
            print("***** Not a valid guess. *****\n")

        # display the required design(hangman) corresponding to the lifeline a available
        print(display_hangman(tries))

        # display all the letters that are guessed correctly
        print(word_completion)

        # new line
        print("\n")

    # if the guessed word matches the actual word
    if guessed:
        print("********** Congrats, you guessed the word! You win! **********\n")

    # if the user gets out of tries(lifeline) withot guessing complete word
    else:
        print("********** Sorry, You Died. The word was " + word + ". Better Luck Next Time! **********\n")


# specific design for the hangman game , if complete body of person is displayed that means game over


def display_hangman(tries):

    # specific design list acc to the available lifeline
    stages = [  # final state(full body hanged, the person dies), Game over !
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # 6th state (head, torso, both arms, and one leg), initiated if 5 letters are guessed wrong
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # 5th state (head, torso, and both arms), initiated if 4 letters are guesssed wrong
                """
                   ________
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # 4th state (head, torso, and one arm), initiated if 3 letters are guesssed wrong
                """
                   ________
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # 3rd state (head and torso), initiated if 2 letters are guessed wrong
                """
                   ________
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # 2nd state (the head), initiated if a letter is guessed wrong
                """
                   ________
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # 1st state (only the hanger), initiated at the start of game
                """
                   ________
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    # return the specific design corresponding to the current lifeline
    return stages[tries]

# driver function to initiate the game acc. to users input (yes/no)


def main():
    # get the word from the word list
    word = get_word()

    # begin the game with the word stored above(random)
    play(word)

    # keep on playing until users hits No ('N')
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

print("\n")
