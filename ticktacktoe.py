board=["1","2","3","4","5","6","7","8","9"]
player=["X","O"]
turn=0
winner=None
gamerunning=1


#-----------------------print board-----------------------
def printboard():
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|---|---|---|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|---|---|---|")
    print("|",board[6],"|",board[7],"|",board[8],"|")
#----------------------take input-----------------------------
def takeinp():
    
    print(player[turn],"\'s turn ")
    inpval=int(input("enter the position"))
    if board[inpval-1] == "X" or board[inpval-1] == "O":
        print("position already taken")
    elif inpval<1 or inpval>9:
        print("wrong input try again")
    else:
         
        board[inpval-1]=str(player[turn])
        return
        

#------------------------check winner---------------------------
def checkwin():
    global winner
    global gamerunning
    for i in range(3):
        if (board[i]==board[i+3]==board[i+6]=="X")or(board[i]==board[i+3]==board[i+6]=="O"):
            winner=board[i]
            gamerunning=0
            return 
    for i in range(0,7,3):
        if (board[i]==board[i+1]==board[i+2]=="X")or(board[i]==board[i+1]==board[i+2]=="O"):
            winner=board[i]
            gamerunning=0
            return
    if (board[0]==board[4]==board[8]=="X") or (board[0]==board[4]==board[8]=="O"):
        winner=board[0]
        gamerunning=0
        return
        if (board[2]==board[4]==board[6]=="X") or (board[2]==board[4]==board[6]=="O"):
            winner=board[0]
            gamerunning=0

#---------------------game-------------------

while(gamerunning):
    printboard()
    takeinp()
    checkwin()
    turn=int(not(turn))
print("-------------------------------------------game over--------------------------------------- ")
print("the winner is  ",winner)

        


