import random

def stunned():
    messa = ["Did You See Those Stars?","Whhhhaaaaaa!!!!",
             "Why Is There Two Of Em Now!?!","Check Please.",
             "Eeny, Meeny, Miny, Whoaaa!!","Is There Doctor In The House!" 
             ]
    print(random.choice(messa))
    hit=0
    return hit



stat_switch={
    "stun":stunned
    }



