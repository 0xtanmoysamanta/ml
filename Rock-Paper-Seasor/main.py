import random
print("Welcome to the rock paper seasor game")


    
usr = input ('Type : rock (r) , paper(p) , seasor(s) :\t')
com = random.randint(1,3)

if com == 1 :
    computer = 'r'

if com == 2 :
    computer= 'p'

if com== 3 :
    computer='s'

def GameWon(usr,computer):
    if (usr =='r' ):
        if computer=='p':
#              print("computer won!")
             return "Computer won!"
        elif computer =='s':
#              print("You won!")
             return "You won!"
        else:
#              print("Tide!")
             return "Tide"
    elif (usr =='p' ):
        
        if computer=='r':
#              print("You won!")
             return "You won!"
        elif computer =='s':
             
#             print("Computer won!")
             return "Computer won!"
        else:
#            print("Tide!")
             return "Tide"
    elif (usr =='s' ):
        if computer=='r':
#               print("Computer won!")
             return "Computer won!"
        elif computer =='p':
#              print("You won!")
             return "You won!"
        else:
#              print("Tide!")
             return "Tide"
with open("score.tex", 'a', encoding ='utf-8', ) as Fil:
    Fil.write(f"You type : {usr}")
    Fil.write("Computer type : {computer}")
    Fil.write(f"Result : {GameWon(usr,computer)}")
    
print("You type :\t" + usr)
print("Computer type:\t" + computer)
print(GameWon(usr,computer))
