import random


def peashooter(): #case peashooter
    ps= []
    for x in range(1,5):
        ps.append(x)
    chance = random.randint(1,100)
    if chance > 97:
        hit = random.choice(ps)
        hit = hit *2+6
        print("Critical Hit!")
    elif chance > 80:
        hit = sum(random.sample(ps,2))
        print("The Peashooter Gets Two Shots Off.")
    elif chance <=80 and chance >=10:
        hit = random.choice(ps)
        print("The Shot Lands.")
    elif chance < 10 and chance >= 5:
        hit = random.choice(ps)
        hit -=1
        print("The Bullet Only Grazes.")
    else:
        hit = 0
        print("The Shot Goes Wild And Misses Completely!")
    ps.clear()
    print(hit,"Damage.")
    return hit

#switch[]()
weapons ={
    "peashooter":peashooter
    }
