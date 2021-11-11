# rock paper scissor game
import random
import os
# from os.path import exists
import os.path
clear = lambda: os.system('cls')
# def game():
    # return win
def gamewin(comp,you):
    if comp==you:
        return None
    
    elif comp== 'r':
        if you=='s':
            return False
        elif you== 'p':
            return True
    
    elif comp== 'p':
        if you=='r':
            return False
        elif you== 's':
            return True

    elif comp== 's':
        if you=='p':
            return False
        elif you== 'r':
            return True       


print("computer turn: rock(r), paper(p), scissor(s)") 

hiscore=''
win=0
while (1):

    you= input("Your turn:rock(r), paper(p), scissor(s)= ")
    if you=='r' or you =='p' or you=='s':
        print(f"you chose ={you}")
        randNo = random.randint(1,3)
        if randNo==1:
            comp='r'
        elif randNo==2:
            comp='p'
        elif randNo==3:
            comp='s'
        print(f"computer chose={comp}")
        a=gamewin(comp,you)
        
        if a==None:
            print("game is tie")
        elif a:
            print("you win")
            win+=1
        else:
            print("you lose")

        print(f"you win {win} times")

    else:
        print("you entered wrong key, pls enter correct key")

    mykey= input("Enter e/E to exit and any key to continue...")
    if mykey=='E' or mykey=='e' :
        your_score = win
        if os.path.exists('hiscore.txt'):
            with open('hiscore.txt') as f:
                hiscore= f.read()

        if hiscore=='':
            with open('hiscore.txt','w') as f:
                f.write(str(your_score))

        elif int(hiscore) < your_score:
            with open('hiscore.txt','w') as f:
                f.write(str(your_score))
        break
    else:
        clear()

    
    