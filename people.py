from images import *

key_words = ["bye"]

arlo_speech = {
"arlo":"Yea?",
"nakkita":"She Runs A Bar In The South East Area Here Downtown.",
"default": "Did you see the news?, the ALLIANCE busted a huge counterfiet ID_CARD operation.",
"alliance":"Are you new? The Alliance run the inner planets, and have major influence on how planets on the rim are run, although the BROWNCOATS dont take much to that.",
"id card":"Everyones got em, standard issue that is, Alliance issued cards come with some extra perks.",
"browncoats":"When the border planets seceded from the Central Core, the ensuring conflict was known as he Unification War. \n\
Soldiers of the outer planets had little resources, hence the brown leather they wore in the battlefield.\n\
The war went poorly for them, now most of them work odd JOBS for a living.",
"jobs":"I don't have anything for you, If you look you can find work in most any area though.",
"dunknow":" I havn't heard much of that!"
}

arlo_KW ={
    "default":"alliance," + " id card",
    "alliance":"browncoats",
    "browncoats":"jobs"
}


def speak(person_bust,person_speech,person_keywords,say="default"):
    in_convo = True
    while in_convo == True:
        print("\n"*70)

        if say in person_speech:
            print(person_bust)
            print(person_speech.get(say))
        elif say == "bye":
            break
        else:
            print(person_bust)
            print(person_speech.get("dunknow"))
        print("__"*80)
        if say in person_keywords:
            kw = person_keywords.get(say)
            if len(kw) > 0:
                if kw not in key_words:
                    key_words.append(kw)
        say = player_speak()
        say = say.lower()

 
def player_speak():
    print(player_bust)
    print("Key Words = ",end="")
    for item in key_words:
        print(item,end=", ")
    say = input("\n>")
    return say



