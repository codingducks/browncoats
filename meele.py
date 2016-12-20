from player_battle_menu import *
from fightfunctions import *
from player_stat import *
from arlo import *

def key_pressed(char_width=1):
    import os, sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(char_width)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def player_turn():
    main = True
    while main == True:
        player_battle("main")
        kp= key_pressed()
        if kp == "1":
            hit = attk(player_equipment)
            spcl=None
            main=False

        elif kp =="2":
            skill = True
            while skill == True:
                print("\n"*70)
                player_battle("skills")
                sp = key_pressed()
                if sp.isdigit()==False:
                    continue
                elif sp == "9":
                    break
                else:
                    pass
                
        elif kp == "3":
            item = True
            while item == True:
                print("\n"*70)
                player_battle("items")
                ip = key_pressed()
                if ip.isdigit()==False:
                    continue
                if ip == "9":
                    break
                else:
                    hit=0
                    item = item_switch[ip]
                    if player_items.get(item) >0:
                        print("You Use a",item)
                        kp_switch[ip](item,player_cur,player_items,player_maxhp,player_maxmp)
                        main = False
                    else:
                        print("You Have No", item)
        elif kp == "9":
            break
        if main == False:
            return hit
                    

def fight():

    while True:
        print("\n"*70)
        arlo_bat(arlo_stat.get("HP"))
        hit= player_turn()
        calc_damg(hit,arlo_stat)
        key_pressed()
        print("_"*10)
        hit = arlo_turn()
        calc_damg(hit,player_cur)
        
        key_pressed()

fight()



