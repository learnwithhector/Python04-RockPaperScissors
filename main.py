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

import random
c = str(random.randint(0,2)) # c is computer choice

print("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.")
p = input() # p is player choice

if p == '0':
    print(rock)
elif p == '1':
    print(paper)
elif p == '2':
    print(scissors)


print("Computer chose:")

if c == '0':
    print(rock)
elif c == '1':
    print(paper)
elif c == '2':
    print(scissors)

if p == c:
    print("It's a draw")
elif (p == '0' and c == '2') or (p == '1' and c == '0') or (p == '2' and c == '1'):
    print("You win!")
else:
    print("You lose!")

