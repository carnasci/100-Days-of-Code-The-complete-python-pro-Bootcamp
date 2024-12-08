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

rps = [rock, paper, scissors]

pc_choice = random.randint(0, 2)

print(rps[pc_choice])

player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
print(rps[player_choice])

if player_choice == pc_choice:
    print("Computer chose:")
    print(rps[pc_choice])
    print("Tie!")

if player_choice == 0 and pc_choice == 1:
    print("Computer chose:")
    print(rps[1])
    print("You lose!")

if player_choice == 0 and pc_choice == 2:
    print("Computer chose:")
    print(rps[2])
    print("You win!")

if player_choice == 1 and pc_choice == 0:
    print("Computer chose:")
    print(rps[0])
    print("You win!")

if player_choice == 1 and pc_choice == 2:
    print("Computer chose:")
    print(rps[2])
    print("You lose!")

if player_choice == 2 and pc_choice == 1:
    print("Computer chose:")
    print(rps[1])
    print("You win!")

if player_choice == 2 and pc_choice == 0:
    print("Computer chose:")
    print(rps[0])
    print("You lose!")
