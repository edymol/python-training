import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
letters_picked = []

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
display = ["_" for _ in range(word_length)]

# Main game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Update the display with the correctly guessed letter
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
    else:
        # If the guessed letter is not in the chosen word, decrease the lives count
        lives -= 1
        # Print the corresponding hangman stage
        print(stages[lives])

    letters_picked.append(guess)

    if guess in letters_picked:
        lives -= 1
        print("If you pick same letter twice it reduces your life")

    # Print the current display
    print(display)

if lives == 0:
    print("You lose")
else:
    print("You win!")
