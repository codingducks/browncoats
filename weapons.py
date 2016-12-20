import random


def peashooter(on_its_own="True"): #case peashooter
    ps= []
    for x in range(1,5):
        ps.append(x)
    chance = random.randint(1,100)
    if chance > 97:
        hit = random.choice(ps)
        hit = hit *2+6
        if on_its_own=="True":
            print("Critical Hit!")
    elif chance > 80:
        hit = sum(random.sample(ps,2))
        if on_its_own=="True":
            print("The Peashooter Gets Two Shots Off.")
    elif chance <=80 and chance >=10:
        hit = random.choice(ps)
        if on_its_own=="True":
            print("The Shot Lands.")
    elif chance < 10 and chance >= 5:
        hit = random.choice(ps)
        hit -=1
        if on_its_own=="True":
            print("The Bullet Only Grazes.")
    else:
        hit = 0
        if on_its_own=="True":
            print("The Shot Goes Wild And Misses Completely!")
        else:
            print("Lousy")
    ps.clear()
    if on_its_own=="True":
        print(hit,"Damage.")
    return hit

#switch[]()
weapons ={
    "peashooter":peashooter
    }
