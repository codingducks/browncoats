import random
from player_stat import *
from fightfunctions import *

def Fake_Out(who):

    false = "False"
    mp = player_cur.get("MP")
    x = random.randint(1,11)
    print(x)
    if x in range(1,5):
        print( "Bad Shot.")
        spcl = "stun"
        hit = attk(player_equipment,false)
        if hit >= 2:
            hit-=2
        else: hit = 0
        newmp=mp-5
        player_cur["MP"] = newmp
        print(hit,"Damage.")
    elif x in range(5,11):
        print("It Lands.")
        spcl="stun"
        hit = attk(player_equipment,false)
        hit+=4
        newmp=mp-5
        player_cur["MP"] = newmp 
        print(hit,"Damage.")
    elif x == 11:
        print("Great Shot!")
        spcl="stun"
        hit = attk(player_equipment,false)
        hit=hit*3-2
        newmp=mp-5
        player_cur["MP"] = newmp
        print(hit,"Damage.")
    return hit,spcl


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

skill_switch={
    
    }
