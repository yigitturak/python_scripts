import random

computer = random.choice(['scissors', 'rock', 'paper'])
user = input("do you want to choose rock, paper or scissors?\n")
if computer == user:
    print ('TIE')
elif user == 'rock' and computer=='scissors':
    print ('WIN, the computer had ' + computer)
elif user == 'paper' and computer=='rock':
    print('WIN, the computer had ' + computer)
elif user=='scissors' and computer == 'paper':
     print('WIN, the computer had ' + computer)
else:
    print ('User lose and Computer win, Computer had ' + computer)
