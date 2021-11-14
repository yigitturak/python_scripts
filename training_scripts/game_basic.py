computer = 'scissors'
user = input("do you want to choose rock, paper or scissors?\n")
if computer == user:
    print ('TIE')
elif user == 'rock' and computer=='scissors':
    print ('WIN')
elif user == 'paper' and computer=='rock':
    print('WIN')
elif user=='scissors' and computer == 'paper':
     print('WIN')
else:
    print ('User lose and Computer win')
