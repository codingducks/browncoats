from player_stat import *
from fightfunctions import *
from weapons import *
from items import *

arlo_stat = {"HP":60,"MP":20,"status":"normal"}
maxh=60
maxm=20
arlo_equipment = {"gun":"peashooter"}

arlo_items={"Tylenol":2,
            "Med Patch":1,
            "Med Spray":0,
            "Red Bull":1,
            "Dexadrine":0,
            "Intracardiac Shot":0,
            "Elixer":1,
            "Elix-all":0}


def normal_shot():
    print("")
    print("Arlo Shoots\n")
    hit =attk(arlo_equipment)
    return hit   

def multishot():
    print("")
    print("Arlo Uses Multishot\n")
    if arlo_stat.get("status") =="normal":
        hit1 = attk(arlo_equipment)
        hit2 = attk(arlo_equipment)
        hit3 = attk(arlo_equipment)
        hit = hit1+hit2+hit3
        arlo_stat["MP"] = arlo_stat.get("MP")-5
        return hit


def use_multishot_if_can(mp,redbull,maxh,maxm):
    hit=0
    if mp > 10:
        hit = multishot()
    elif mp <=10 and redbull == 0:
        if mp - 5 > 0:
            hit = multishot()
        else:
            hit= normal_shot()
    elif mp <=10 and redbull > 0:
        x = random.randint(1,2)
        if x == 1:
            print("Arlo Drinks A Redbull")
            Heal_Item("Red Bull",arlo_stat,arlo_items,maxh,maxm)
        elif x == 2:
            hit = normal_shot()
    else:
        hit = normal_shot()
    return hit
            


def arlo_turn():
    hit=0
    print("ARLO'S TURN")
    tylenol = arlo_items.get("Tylenol")
    medpatch = arlo_items.get("Med Patch")
    redbull = arlo_items.get("Red Bull")
    elixer = arlo_items.get("Elixer")
    hp= arlo_stat.get("HP")
    mp= arlo_stat.get("MP")
    if hp >=40:
        hit = use_multishot_if_can(mp,redbull,maxh,maxm)
    elif hp <40 and hp >=30:
        x= random.randint(1,3)
        if x == 1:
            if tylenol >0:
                print("Arlo Takes A Tylenol.")
                Heal_Item("Tylenol",arlo_stat,arlo_items,maxh,maxm)
            else:
                hit = use_multishot_if_can(mp,redbull,maxh,maxm)
        else:
            hit= use_multishot_if_can(mp,redbull,maxh,maxm)
    elif hp <30 and hp >=20:
        x= random.randint(1,3)
        if x == 2 or x == 3:
            if medpatch >0:
                print("Arlo Applies A Med Patch.")
                Heal_Item("Med Patch",arlo_stat,arlo_items,maxh,maxm)
            elif tylenol >0:
                print("Arlo Takes A Tylenol.")
                Heal_Item("Tylenol",arlo_stat,arlo_items,maxh,maxm)
            else:
                hit= use_multishot_if_can(mp,redbullmaxh,maxm)
        else:
            hit= use_multishot_if_can(mp,redbull,maxh,maxm)
    elif hp <20:
        if elixer >0:
            print("Arlo Drinks An Elixer")
            Elixer(arlo_stat,arlo_items,maxh,maxm)
        elif medpatch >0:
            print("Arlo Applies A Med Patch.")
            Heal_Item("Med Patch",arlo_stat,arlo_items,maxh,maxm)
        elif tylenol >0:
            print("Arlo Takes A Tylenol.")
            Heal_Item("Tylenol",arlo_stat,arlo_items,maxh,maxm)
        else:
            hit= use_multishot_if_can(mp,redbull,maxh,maxm)

    return hit
        
                

def arlo_bat(hp):
    hphimes=["Gorram Fool!","You Cant Win.","Babes In A Basket, You are."]
    hplowmes = ["Muqīn tā mā de, I'll still win.","So, You Got A Good Shot."]
    if hp > 25:
        message= random.choice(hphimes)
    else:
        message = random.choice(hplowmes)
    a=" ___________________ "
    b="|    // ======= \]  |"  
    c="|   ||/         \|| |"
    d="|   | .-==_ _==-. | |"
    e="|  _|  -o-   -o-  |_|"
    f="|  ||     / \     |||"
    g="|  \|    '-_-`    |/|"
    h="|    |   _===_   |  |"
    i="|    |  |-___-|  |  |"
    j="|     \ |.....| /   |"
    k="|      `-|||||-.    |"
    l="|                   |"
    m=" ___________________ "
    arlo_lis= []
    arlo_lis.extend((a,b,c,d,e,f,g,h,i,j,k,l,m))

    pic = []
    for r in range(15):
        row = []
        for c in range(13):
            row.append(" ")
        pic.append(row)
    for x in range(0,13):
        pic[x][0] = arlo_lis[x]
    for x in range(0,8):
        pic[0][x]="_____________"
    for x in range(2,8):
        pic[2][x]="______________"

    pic[1][3] = "Arlo Smother"
    pic[4][2] = '"' * hp 
    pic[4][4] = "HP"
    pic[9][3] = "       "
    pic[9][4] = message
    for x in range(0,12):
        pic[12][x] = "_________"

            
    for row in range(15):
      for col in range(13):
          token = pic[row][col]
          if not token:
              token = ""
          print(token,end="")
      print()





