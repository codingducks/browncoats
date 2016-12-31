from player_battle_menu import *
from fightfunctions import *
from player_stat import *
from enemies import *
from skills import *





def player_turn(enemy):
    main = True
    while main == True:
        player_battle("main")
        kp= key_pressed()
        if kp == "1":
            who= enemy
            hit = attk(player_equipment,who)
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
                    who=enemy
                    if sp in kp2_switch:
                        skill=kp2_switch[sp]
                        if skill_mp.get(skill) <= player_cur.get("MP"):
                            hit= string_2_func[skill](who)
                            main=False
                        else:
                            print("You Don't Have The Energy To Use",skill )
                            key_pressed()
                            continue
                    else:
                        continue
                
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
            hit=0
            main=False
        if main == False:
            return hit
                    

def fight(enemy):
    fight = True
    while fight == True:
        print("\n"*70)
        arlo_bat(enemy.get("HP"))
        hit= player_turn(enemy)
        calc_damg(hit,player_cur,enemy)
        if enemy.get("HP") <=0:
            fight = False
        key_pressed()
        print("_"*10)
        hit = arlo_turn()
        calc_damg(hit,enemy,player_cur)
        if player_cur.get("HP") <=0:
            fight = False
        
        key_pressed()

#fight(arlo_stat)



