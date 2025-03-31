import random
import hang_man

# List of words to choose from
word_list = ["penguin", "thunder", "cactus", "journey", "whisper", "falcon", "galaxy", "pumpkin", "lantern", "shadow"]

# Randomly select a word
chosen_word = random.choice(word_list)
print(chosen_word)

display_word = ["_"] * len(chosen_word)  # Placeholder for unguessed letters

lives = len(chosen_word) -1

stage_num = 0

print("Welcome to the word guessing game!")
print(" ".join(display_word))

while lives > 0 and "_" in display_word:
    guess = input("\nGuess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[index] = guess
        print("Good guess!")
        # Check win or loss condition
        if "_" not in display_word:
            print(f"You guessed the word: {''.join(display_word)} 🎉")
            print(f"\nCongratulations! ****************************YOU WIN****************************")
    else:
        print(hang_man.stages[stage_num])
        lives -= 1
        stage_num += 1
        print(f" Wrong guess!\n ****************************<???>/{lives} LIVES LEFT****************************")


    if lives == 0:
        #print(f"\nGame over! The correct word was: {chosen_word} 😢")
        print(f"************GAME OVER!  YOU LOSE**********************\n The correct word was: {chosen_word} 😢")




