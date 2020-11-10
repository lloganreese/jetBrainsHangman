import random

print("H A N G M A N")

while True:
    selection = input('Type "play" to play the game, "exit" to quit: ')
    if selection == "play":
        x = 0
        secret_list = ('python', 'java', 'kotlin', 'javascript')
        secret_word = random.choice(secret_list)
        user_list = len(secret_word) * "-"
        guessed_letters = []
        while x <= 7:
            print("\n" + user_list)
            user_input = input("Input a letter: ")

            if 2 <= len(user_input) or len(user_input) == 0:
                print("You should input a single letter")
                guessed_letters.append(user_input)
            elif user_input.isupper() or not ('a' <= user_input <= 'z'):
                print("Please enter a lowercase English letter")
                guessed_letters.append(user_input)
            elif user_input in guessed_letters:
                print("You've already guessed this letter")
            elif user_input in secret_word:
                r = 0
                while r < len(secret_word):
                    if secret_word[r] == user_input:
                        user_list = list(user_list)
                        user_list[r] = secret_word[r]
                        user_list = "".join(user_list)
                    r += 1
                guessed_letters.append(user_input)
            elif user_input not in secret_word:
                print("That letter doesn't appear in the word")
                guessed_letters.append(user_input)
                x += 1

            if user_list == secret_word:
                print(user_list)
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You lost!")
    elif selection == "exit":
        exit()
    else:
        print("Incorrect Input")
