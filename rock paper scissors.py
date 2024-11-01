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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissor)
else:
    print("It's an invalid number. You lose.")

computer_choice = random.randint(0, 2)

print("Computer chose:\n")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissor)

if choice == computer_choice:
    print("It's a draw.")
elif choice == 0 and computer_choice == 2:
    print("You win.")
elif choice == 1 and computer_choice == 0:
    print("You win.")
elif choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("You lose.")