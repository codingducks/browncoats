from weapons import *

def attk(play_equip,on_its_own="True"):
    gun = play_equip.get("gun")
    hit = weapons[gun](on_its_own)
    return hit

def calc_damg(hit,who):
    hp = who.get("HP")
    hp -= hit
    who["HP"] = hp
