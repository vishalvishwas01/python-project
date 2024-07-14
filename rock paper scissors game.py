import random
l=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
game start...
1 yes
2 no 
    '''))

    if uc==1:
        for a in range(1,6): # 5 rounds game
            userinput=int(input('''
1 rock
2 scissor
3 paper
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif ((uchoice=="rock" and cchoice=="scissor") or
                  (uchoice=="paper" and cchoice=="rock") or
                  (uchoice=="scissor" and cchoice=="paper")):
                print("computer value",cchoice)
                print("user value",uchoice)
                print("user win")
                ucount=ucount+1

            else:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("computer win")
                ccount=ccount+1

        if ucount==ccount:
            print("")
            print("final game draw")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("")
            print("......you win the game........")
            print("user score", ucount)
            print("computer score", ccount)
        else:
            print("")
            print("......computer win the game........")
            print("user score", ucount)
            print("computer score", ccount)
    else:
        break