from hero import *
from theTavern import *
from taskManager import *
import time

def checkInp(s):
    if s!="move" and s!="view" and s!="fight" and s!="wait" and s!="opt" and s!="esc" and s!="buy":
        return False
    return True

def options():
    print("move : move heroes to a floor to improve stats")
    print("view : view the next monster, your heroes, or the tavern as a whole")
    print("fight : send your heroes to fight the monster and bring glory to the tavern!")
    print("wait : if you just want the tower to continue what it's doing")
    print("buy : use your gold to summon a new hero to your tavern")

def doTheThing(s,tav,tasks):
    s = s.lower()
    if s=="move":
        move(tav, tasks)
    elif s=="view":
        view(tav)
    elif s=="fight":
        fight(tav,tasks)
    elif s=="opt":
        options()
    elif s=="buy":
        if tav.gold>= 100:
            tav.newHero()
    else:
        time.sleep(1)
        tasks.do(tav)
        

def move(t, tasks):
    valid = False
    while valid == False:
        h = input("Who do you want to move? ")
        for x in t.getHeroList():
            if h==x.name:
                valid = True
                h = x
                break
        if valid == False:
            print("Not a valid hero name")

    valid = False
    while valid == False:
        print("Places they can go: library, training room, inn")
        p = input("Where do you want them to be moved to? ")
        p = p.lower()
        if p=="library" or p=="training room" or p=="inn":
            valid = True
    if p == "library":
        t.library(x,tasks)
    if p == "training room":
        t.train(x,tasks)
    if p == "inn":
        t.rest(x,tasks)

def view(t):
    valid = False
    while valid == False:
        view = input("Would you like to view the next monster(mons), your hero stats(hero), or the overall tavern(tav)? ")
        if view == "mons" or view=="hero" or view=="tav":
            valid = True
    if view == "mons":
        t.viewNextMons()
    if view == "hero":
        t.viewHeroes()
    if view == "tav":
        print(str(t))

def fight(t,tas):
    sure = input("Are you sure you are ready? (y/n) ")
    if sure == "y":
        t.fight(tas)

    
print("Welcome to IdleTavern!")
main = theTavern()
tasks = taskManager()
print("This is your tavern. I know you can't see a tavern, but imagine it bustling with travellers, and there they are, your heroes!")
print(str(main))
print("Looks like we need to fix some things.",end=" ")
user = input("First off, what is your name? ")
main.setUser(user)
print("You get to start with two brave adventurers.",end=" ")
user = input("What do you want the Wizard's name to be? ")
user += " "+input("What do you want the Warrior's name to be? ")
user = user.split(" ")
main.setStartHeroes(user[0],user[1])
print("\nOkay, now let's take a look at the tavern:\n",str(main))
print("\n\nLooking better! Now, let's learn about your heroes. Here's their stats:")
main.viewHeroes()
print("Each hero has Intelligence and Strength Points. You can better these by sending your heroes to the library or the training room.")
print("They also each have hit points, or how healthy they are.")
print("They are at max hp currently, but after battle send them to the inn to rest.")
print("Battle? Yes, the heroes do actually battle. Let's look at their next mission:")
main.viewNextMons()
print("Yikes. The monsters each have intelligence and strength scores.")
print("Your heroes must combine their stats to beat the monster. Be warned, your heroes can die.")
print("\n\nNow what are you going to do? You have lots of options.")
options()
act = input("What do you want to do? ")
while not checkInp(act):
    act = input("Invalid - Please choose an option from the list. ")
print("Nice choice!")
doTheThing(act,main,tasks)
print("\n\n")
while act!="esc":
    act = input("Choose an action: (type opt for actions) ")
    while not checkInp(act):
        act = input("Invalid - Please choose a valid action: ")
    doTheThing(act,main,tasks)
    print("\n")
