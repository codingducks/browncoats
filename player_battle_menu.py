from player_stat import *

def args(which_menu):
    if which_menu == "main":
        options = {
        'arg1':"1) Fight  ",
        'arg2':"2) Skills ",
        'arg3':"3) Items  ",
        'arg4':"     ",
        'arg5':"        ",
        'arg6':"        ",
        'arg7':"      ",
        'arg8':"        ",
        'arg9':"9) Pass   ",}
        return options
    elif which_menu == "items":
        options = {
        'arg1':"1) Tylenol  ",
        'arg2':"2) Med Patch",
        'arg3':"3) Med Spray",
        'arg4':"4) Red Bull ",
        'arg5':"5) Dexadrine",
        'arg6':"6) Intracardiac Shot",
        'arg7':"7) Elixer",
        'arg8':"8) Elix-all",
        'arg9':"9) Pass   ",}
        return options
    elif which_menu == "skills":
        options = {
        'arg1':"",
        'arg2':"",
        'arg3':"",
        'arg4':"",
        'arg5':"",
        'arg6':"",
        'arg7':"",
        'arg8':"",
        'arg9':"9) pass",}
        x=1
        for i in skills:
            options["arg"+str(x)] = str(x)+")" + " "+i
            x+=1
        return options

def item_amounts(pic):
    for x in range(6,12,2):
        pic[x][3] = " X"
        pic[x][7] = " X"
    pic[6][4] = player_items.get("Tylenol")
    if player_items.get("Tylenol") == 0:
        pic[6][4] = "0"
    pic[8][4] = player_items.get("Med Patch")
    if player_items.get("Med Patch") == 0:
        pic[8][4] = "0"
    pic[10][4] = player_items.get("Med Spray")
    if player_items.get("Med Spray") == 0:
        pic[10][4] = "0"

    pic[6][8] = player_items.get("Red Bull")
    if player_items.get("Red Bull") == 0:
        pic[6][8] = "0"
    pic[8][8] = player_items.get("Dexadrine")
    if player_items.get("Dexadrine") == 0:
        pic[8][8] = "0"
    pic[10][8] = player_items.get("Intracardiac Shot")
    if player_items.get("Intracardiac Shot") == 0:
        pic[10][8] = "0"

    for x in range(6,10,2):
        pic[x][11] = " X"
    pic[6][12] = player_items.get("Elixer")
    if player_items.get("Elixer") == 0:
        pic[6][12] = "0"
    pic[8][12] = player_items.get("Elix-all")
    if player_items.get("Elix-all") == 0:
        pic[8][12] = "0"

    for x in range(6,12,2):
        pic[x][5]="     "
    for x in range(7,13,2):
        pic[x][5]="               "
    for x in range(6,12,2):
        pic[x][9]="               "
    for x in range(7,13,2):
        pic[x][9]="               "
    return pic

def skills_mp(pic):
    temp=[]
    for i in skills:
        temp.append(i)
    y=0
    for x in range(6,12,2):
        if pic[x][1] != "":
            pic[x][3] = " MP:"
            pic[x][4] = skill_mp.get(temp[y])
            y+=1
    for x in range(6,12,2):
        if pic[x][6] != "":
            pic[x][7] = " MP:"
            pic[x][8] = skill_mp.get(temp[y])
            y+=1
    for x in range(6,10,2):
        if pic[x][10] != "":
            pic[x][11] = " MP:"
            pic[x][12] = skill_mp.get(temp[y])
            y+=1

    for x in range(6,12,2):
        pic[x][5]="     "
    for x in range(7,13,2):
        pic[x][5]="               "
    for x in range(6,12,2):
        pic[x][9]="               "
    for x in range(7,13,2):
        pic[x][9]="               "
    return pic

def main(pic):

    for x in range(6,12,2):
        pic[x][5]="     "
    for x in range(7,13,2):
        pic[x][5]="               "
    for x in range(6,12,2):
        pic[x][9]="               "
    for x in range(7,13,2):
        pic[x][9]="               "

    return pic

menus ={"items":item_amounts,
        "skills":skills_mp,
        "main":main
        }

def player_battle(which_menu):
    options = args(which_menu)

    a=" ____________________"
    b="|      .x%%%%%%x.   |"
    c="|     ,%%%%%%%%%%%  |"
    d="|    ,%%%'  )'  \%  |"
    e="|   ,%x%) __   _ Y  |"
    f="|   :%%% ~=-. <=~|  |"
    g="|   :%%::. .:,\  |  |"
    h="|   `;%:`\. `-' .'  |"
    i="|    ``x`. -===-;   |"
    j="|     / `:`.__.;    |"
    k="|  ._/\.  :: ..`.   |"
    l="| ./  ^\_.  '  /L   |"
    m=" ____________________"

    play_lis =[]
    play_lis.extend((a,b,c,d,e,f,g,h,i,j,k,l,m))

    pic = []


    for r in range(15):
        row = []
        for c in range(13):
            row.append(" ")
        pic.append(row)

    for x in range(0,13):
        pic[x][0] = play_lis[x]
    for x in range(0,8):
        pic[0][x]="_____________"
    for x in range(2,8):
        pic[2][x]="______________"
    pic[1][3] = " "+player_name
    pic[4][1] = " "+"HP "+ str(player_cur.get("HP")) +"/" +str(player_maxhp)
    pic[4][3] = " "+"MP "+ str(player_cur.get("MP")) +"/" +str(player_maxmp)
    pic[4][4] = "     "
    pic[4][5] = "Status: "+str(player_cur.get("status")) 
    pic[6][1] = options['arg1']
    pic[8][1] = options['arg2']
    pic[10][1] = options['arg3']
    pic[6][6] = options['arg4']
    pic[8][6] = options['arg5']
    pic[10][6] = options['arg6']
    pic[6][10] = options['arg7']
    pic[8][10] = options['arg8']
    pic[10][10] = options['arg9']


    pic = menus[which_menu](pic)

            
    for row in range(15):
      for col in range(13):
          token = pic[row][col]
          if not token:
              token = ""
          print(token,end="")
      print()
