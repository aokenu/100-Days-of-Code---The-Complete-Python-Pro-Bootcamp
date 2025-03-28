import random


# TODO-1: - Use a while loop to let the user guess again.

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

word_list = ["penguin", "thunder", "cactus", "journey", "whisper", "falcon", "galaxy", "pumpkin", "lantern", "shadow"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

if guess in chosen_word:
    print("Right")
else:
    print("Wrong")

# Create a placeholder for the word
placeholder = ["_" for _ in chosen_word]
print(" ".join(placeholder))
