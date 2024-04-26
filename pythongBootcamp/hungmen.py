# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
# the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.
# Create a while to either win or loose the game

display = ["_" for _ in range(word_length)]

# Main game loop
while "_" in display:
    guess = input("Guess a letter: ").lower()

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess

    # Print the display list
    print(display)

print("You win!")  # This line will be executed when the loop ends because all letters have been guessed
# print("guess: ", guess, " - letter count :", count)
