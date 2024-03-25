import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

shapes = [rock, paper, scissors]

player_choice = int(input("What do you choose? 1 for Rock, 2 for Paper, or 3 for Scissors: "))

# Ensure the player's choice is within a valid range
if 1 <= player_choice <= 3:
    player_choice = shapes[player_choice - 1]
    print(player_choice)
    computer_choice = random.choice(shapes)
    print(f"Computer choice is {computer_choice}")

    if player_choice == computer_choice:
        print("Draw")
    elif (player_choice == rock and computer_choice == scissors) or \
         (player_choice == paper and computer_choice == rock) or \
         (player_choice == scissors and computer_choice == paper):
        print("Player won")
    else:
        print("Computer won")
else:
    print("Invalid choice. Please choose 1 for Rock, 2 for Paper, or 3 for Scissors.")