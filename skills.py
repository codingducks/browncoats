import random
from player_stat import *
from fightfunctions import *

def Fake_Out(who):
    who['status']='stun'
    mp = player_cur.get("MP")
    x = random.randint(1,11)
    attacker = player_cur
    if x in range(1,5):
        print( "Bad Shot.")
        hit = attk(player_equipment,attacker)
        if hit >= 2:
            hit-=2
        else: hit = 0
        newmp=mp-5
        player_cur["MP"] = newmp
        print(hit,"Damage.")
    elif x in range(5,11):
        print("It Lands.")
        hit = attk(player_equipment,attacker)
        hit+=4
        newmp=mp-5
        player_cur["MP"] = newmp 
        print(hit,"Damage.")
    elif x == 11:
        print("Great Shot!")
        hit = attk(player_equipment,attacker)
        hit=hit*3-2
        newmp=mp-5
        player_cur["MP"] = newmp
        print(hit,"Damage.")
    return hit


string_2_func={"Fake Out":Fake_Out
               }

skill_template={
        's1':"",
        's2':"",
        's3':"",
        's4':"",
        's5':"",
        's6':"",
        's7':"",
        's8':"",}
x=1
for i in skills:
    skill_template["s"+str(x)] = i
    x+=1


kp2_switch = {
    "1":skill_template.get('s1')
}

