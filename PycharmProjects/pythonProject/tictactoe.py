#global variable
gameon=True
winner=None
player="X"
#making board
plane=["-","-","-",
       "-","-","-",
       "-","-","-",]
#print(plane)
def display():
    print(plane[0] + " | " + plane[1]+ " | " +plane[2])
    print(plane[3] + " | " + plane[4] + " | " + plane[5])
    print(plane[6] + " | " + plane[7] + " | " + plane[8])

#play game
def play():

    display()
    while gameon:                                                     #play untill any win or tie
        handleturn(player)                                                     #manage how and where to place
        gameover()                                                       #check if game oveer
        flip()                                                                  #change player
    if winner=="X"or winner=="Y" :
        print(winner+" won ")
    elif winner==None:
        print("tie")

def gameover():
    win()
    tie()
def win():
    global winner
    row_win=row()
    col_win=col()
    dia_win=dia()
    if row_win:
        winner=row_win
    elif col_win:
        winner=col_win
    elif dia_win:
        winner=dia_win
    else:
        winner = None
def row():
    r1 = plane[0] == plane[1] == plane[2] != "-"
    r2 = plane[3] == plane[4] == plane[5] != "-"
    r3 = plane[6] == plane[7] == plane[8] != "-"
    global gameon
    if r1 or r2 or r3:
        gameon=False
    if r1:
        return plane[0]
    elif r2:
        return plane[3]
    elif r3:
        return plane[6]
    return
def col():
    c1 = plane[0] == plane[3] == plane[6] != "-"
    c2 = plane[1] == plane[4] == plane[7] != "-"
    c3 = plane[2] == plane[5] == plane[8] != "-"
    global gameon
    if c1 or c2 or c3:
        gameon=False
    if c1:
        return plane[0]
    elif c2:
        return plane[1]
    elif c3:
        return plane[2]
    return
def dia():
    d1=plane[0]==plane[4]==plane[8]!="-"
    d2=plane[6]==plane[4]==plane[2]!="-"
    global gameon
    if d1 or d2:
        gameon=False
    if d1:
        return plane[0]
    elif d2:
        return plane[6]



def tie():
    global gameon
    if "-" not in plane:
        gameon=False
        return True
    else:
        return False

def flip():
    global player
    if player == "X":
       player = "O"
    elif player == "O":
      player = "X"


    return


def handleturn(player):

    print("enter position to enter [1-9]")
    position=int(input())-1
    if(plane[position])=="-":
        plane[position] = player
    else:
        print("enter a valid position")

    display()
play()


