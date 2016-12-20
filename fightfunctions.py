from weapons import *
from status import *

def attk(play_equip,attacker):
    status = attacker.get('status')
    if status == "normal":
        gun = play_equip.get("gun")
        hit = weapons[gun]()
        return hit
    else:
        hit = stat_switch[status]()
        return hit

def calc_damg(hit,attker,attkee):
    hp = attkee.get("HP")
    hp -= hit
    attkee["HP"] = hp
    attker["status"] = 'normal'
