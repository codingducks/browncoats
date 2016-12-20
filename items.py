def Heal_Item(item,whostat,whoitem,whomaxhp,whomaxmp):
    amount = item_amount.get(item)
    hpmp = item_class.get(item)
    if hpmp == "HP":
        whomax= whomaxhp
    elif hpmp=="MP":
        whomax=whomaxmp
    stock = whoitem.get(item)
    if stock == 0:
        print("You Have None.")
    else:
        recov = whostat.get(hpmp)
        recov +=amount
        stock -= 1
        if recov < whomax:
            whostat[hpmp]=recov
        else:
            whostat[hpmp]=whomax
        whoitem[item] = stock



def Elixer(whostat,whoitem,whomaxhp,whomaxmp):
    stock = whoitem.get("Elixer")
    if stock == 0:
        print("You Have None.")

    else:
        whostat["HP"] = whomaxhp
        whostat["MP"] = whomaxmp
        stock -=1
        whoitem["Elixer"] = stock



item_class ={
    "Tylenol":"HP",
    "Med Patch":"HP",
    "Med Spray":"HP",
    "Red Bull":"MP",
    "Dexadrine":"MP"
    }
item_amount ={
    "Tylenol":10,
    "Med Patch":40,
    "Med Spray":100,
    "Red Bull":10,
    "Dexadrine":50
    }
kp_switch={
    "1":Heal_Item,
    "2":Heal_Item,
    "3":Heal_Item,
    "4":Heal_Item,
    "5":Heal_Item,
    }
item_switch={
    "1":"Tylenol",
    "2":"Med Patch",
    "3":"Med Spray",
    "4":"Red Bull",
    "5":"Dexadrine"}
    


