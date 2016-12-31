from ariel import *
from people import *
from meele import *
from enemies import *
from player_stat import *

def key_pressed(char_width=1):
    import os
    #is it a unix-like system?
    if os.name == 'posix': 
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(char_width)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    #is it a windows system?
    elif os.name == 'nt':
        from msvcrt import getch
        return "".join([getch() for i in range(char_width)])
    #system unknown, user will have to use enter key :(
    else:
        return input()


def print_board(town_size,message="",newline_amount=1):
  print("\n"*newline_amount)
  print(message)
  for row in range(town_size):
    for col in range(town_size):
        token = board[row][col]
        if not token:
            token = ""
        print(token,end="")
    print()


def control(current_row,current_col,old_row,old_col,town_size):
    kp = key_pressed()
    if kp.lower() != kp:
        print("No Need To Yell!")
        key_pressed()
    if kp == "j" or kp == "s":
        if current_row <town_size -1:
            if board[current_row + 1][current_col] == empty:
                current_row +=1
    if kp == "k" or kp == "w":
        if current_row > 0:
            if board[current_row -1][current_col] == empty:
                current_row -=1 
    if kp == "h" or kp == "a":
        if current_col >0:
            if board[current_row][current_col - 1] == empty:
                current_col -=1
    if kp == "l" or kp == "d":
        if current_col < town_size -1:
            if board[current_row][current_col +1] == empty:
                current_col +=1
    if kp == " ":
        if current_row <town_size -1 and current_row > 0 and current_col < town_size -1 and current_row > 0:
            print_action_menu()
            
    return current_row,current_col

def game_over(cur_party):
    x=[]
    for person in cur_party:
        if person.get("HP") > 0:
            x.append("alive")
        else:
            x.append("dead")
    if "alive" not in x:
        gameover = True
        x.clear()
        return gameover
    else:
        gameover=False
        x.clear()
        return gameover
    
            

def start_bot(town_size):
    old_row,old_col = 0,0
    current_row = town_size -2
    current_col = int(town_size/2)
    return current_row,current_col,old_row,old_col

def print_action_menu():
    global gameover
    Talk = False
    perimeter = []
    XD = (current_row+1,current_col)
    XU = (current_row-1,current_col)
    YR = (current_row,current_col+1)
    YL = (current_row,current_col-1)
    perimeter.extend((XD,XU,YR,YL))
    for item in perimeter:
        r,c = item[0],item[1]
        if board[r][c] == '@ ':
            Talk = True
            person = item
    
    if Talk == True:
        print('''
        1) Talk
        5) Fight
        Anything Else Exits
        ''')
        kp = key_pressed()
        if kp == "1":
            talk(person)
        elif kp == "5":
            person = people_cords.get(person)
            whom = people_fight.get(person)
            print(whom)
            fight(whom)
            gameover = game_over(cur_party)
            

    elif Talk == False:
        print("There is nothing to do here, but press the enter key!")
        input()


def talk(person):
    if person in people_cords:
        person = people_cords.get(person)
        if person == "Arlo":
            speak(arlo_bust,arlo_speech,arlo_KW)
    
    

player = "@ "
empty = ". "

cur_party = [player_cur]
ariel = 45

ariel_hq = 20
hq_cords = [11,39]

people_cords = {(40,25):"Arlo",
                (21,26):"Nakkita",
                (14,11):"alliguard"
                }
people_fight={
    "Arlo":arlo_stat,
    }


bar = 35
barf_cords = [42,29]
barb_cords =[28,42]

old_row = 0
old_col = 0
current_row = 44   
current_col = 20

gameover=False

playing = True
while playing == True:
    if gameover == True:
        break
    
    board = in_ariel(ariel)
    board[old_row][old_col] = empty     
    board[current_row][current_col] = player      
    print_board(ariel,"ARIEL CITY",75)
    old_row,old_col, = current_row,current_col

    if current_row == hq_cords[0] and current_col == hq_cords[1]:
        current_row, current_col,old_row,old_col = start_bot(ariel_hq)

        inplace = True  #alli HQ
        while inplace == True:
            board = in_ariel_hq(ariel_hq)
            board[old_row][old_col] = empty     
            board[current_row][current_col] = player 

            print_board(ariel_hq,"ALLIENCE HQ",75)
            old_row,old_col, = current_row,current_col

            if current_row == 19 and current_col == 10:
                current_row,current_col = 12,39
                break
            else:
                current_row,current_col = control(current_row,current_col,old_row,old_col,ariel_hq)



    elif current_row == barf_cords[0] and current_col == barf_cords[1] or current_row == barb_cords[0] and current_col == barb_cords[1]:
        if current_row == barf_cords[0] and current_col == barf_cords[1]:
            current_row, current_col,old_row,old_col = 31,1,0,0
        if current_row == barb_cords[0] and current_col == barb_cords[1]:
            current_row, current_col,old_row,old_col = 1,31,0,0

        inplace = True  #BAR
        while inplace == True:
            board = in_bar(bar)
            board[old_row][old_col] = empty     
            board[current_row][current_col] = player 

            print_board(bar,"Nakkita's Bar",75)
            old_row,old_col, = current_row,current_col

            if current_row == 31 and current_col == 0:
                current_row,current_col = 42,28
                break
            if current_row == 0 and current_col == 31:
                current_row,current_col = 27,42
                break
            else:
                current_row,current_col = control(current_row,current_col,old_row,old_col,bar)


    else:
        current_row,current_col = control(current_row,current_col,old_row,old_col,ariel)



print("\n"*70 ,"""
___________________________________________
|                                          |
|          GAME OVER                       |
|                                          |
|                                          |
|                                          |
|                                          |
|                                          |   
|__________________________________________|
""")



