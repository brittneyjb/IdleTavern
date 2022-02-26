#THE TOWER
from hero import *
from monster import *
from taskManager import *
import time


class theTavern:

    def __init__(self):
        self.gold = 100
        self.mons = [Monster("CLASS", 1), Monster("ExamDay", 2), Monster("AP Scorer",3)]
        self.heroes = [Hero("wizard"), Hero("warrior")]
        self.username = " "
        self.lvl = 1
        #floors are 0:Inn 1:Train 2:Library 
        self.hFloors = ["No one","No one","No one"]

    def setUser(self, nm):
        self.username = nm

    def setStartHeroes(self, wi, wa):
        self.heroes[0].setName(wi)
        self.heroes[1].setName(wa)

    def library(self, hero, task):
        hero.setLoc("library")
        if self.hFloors[2] != "No one":
            for x in self.heroes:
                if x.name == self.hFloors[2]:
                    temp = x
            task.delTask(temp)
        if hero in self.hFloors:
            self.hFloors[self.hFloors.index(hero)] = "No one"
        self.hFloors[2] = hero.name
        task.addTask("lib",hero)
        task.do(self)

    def train(self, hero, task):
        hero.setLoc("train")
        if self.hFloors[1] != "No one":
            for x in self.heroes:
                if x.name == self.hFloors[1]:
                    temp = x
            task.delTask(temp)
        if hero in self.hFloors:
            self.hFloors[self.hFloors.index(hero)] = "No one"
        self.hFloors[1] = hero.name
        task.addTask("train",hero)
        task.do(self)


    def rest(self, hero, task):
        hero.setLoc("rest")
        if self.hFloors[2] != "No one":
            for x in self.heroes:
                if x.name == self.hFloors[0]:
                    temp = x
            task.delTask(temp)
        if hero in self.hFloors:
            self.hFloors[self.hFloors.index(hero)] = "No one"
        self.hFloors[0] = hero.name
        task.addTask("rest",hero)
        task.do(self)

    def newHero(self):
        c = input("Would you like a Warrior or a Wizard to move in? (warrior/wizard) ")
        c = c.lower()
        self.heroes.append(Hero(c))
        x = input("What is your "+c+"'s name? ")
        self.heroes[-1].setName(x)
        self.gold-=100

    def viewNextMons(self):
        print(str(self.mons[0]))

    def viewHeroes(self):
        for h in self.heroes:
            print(str(h)+"\n")

    def getHeroList(self):
        return self.heroes

    def fight(self,task):
        task.clearHeroTasks(self)
        bad = self.mons[0]
        fallen = []
        hInt, hStr = 0, 0
        for h in self.heroes :
            hInt+=h.getInt()
            hStr+=h.getStr()
        if hInt > bad.getInt() and hStr > bad.getStr():
            hDec = bad.getHP()*(2/3)
            hDec = hDec // len(self.heroes)
            exp = bad.getHP()//(len(self.heroes)-1)
            for h in self.heroes:
                h.hpDn(hDec)
                h.expUp(bad.getHP()//(exp))
            print("Your brave adventurers fought brilliantly and defeated",bad.getName(),"to gain {} EXP each and {} gold pieces!".format(exp,bad.getGold()))
            print("However,", bad.getName(),"fought back, causing each of your heroes to lose {} HP.".format(hDec))
            self.gold+=bad.getGold()
            self.mons.pop(0)
        elif hInt == bad.getInt() or hInt == bad.getStr():
            hDec = bad.getHP() //len(self.heroes)
            exp = bad.getHP()//(len(self.heroes)-1)
            for h in self.heroes:
                h.hpDn(hDec)
                h.expUp(exp)
            print("Your adventurers barely survived, but they did defeat",bad.getName()+", to gain {} EXP each and {} gold pieces.".format(exp,bad.getGold()))
            print("You earned {}, although your heroes sufferend a loss of {} HP.".format(hDec))
            self.gold+=bad.getGold()
            self.mons.pop(0)
        else:
            for h in self.heroes:
                h.hpDn(bad.getHP())
                h.expUp(bad.getHP()//(len(self.heroes)*2))
            print("You lost bitch\nYour heroes were sent on a mission they could not handle and are now dead or cowards and gained no gold.")             
        for i in range(len(self.heroes)-1,-1,-1):
                if self.heroes[i].getHP()<0:
                    fallen.append(self.heroes.pop(i))
        print("Here are the heroes that fell for the glory of the Tavern:")
        for x in fallen:
            print(x.getName(), end="   ")
        for x in self.heroes:
            x.setLoc("bat")
        hFloors = ["No one", "No one", "No one"]
        print()

    def __str__(self):
        fin = "{}'s Tavern\nGold: {} pieces".format(self.username, self.gold)
        fin+= "\nYour brave heroes:\n"
        for h in self.heroes:
            fin+= str(h.getName())+"\t"
        fin += "\nThe Different Areas: \nThe Inn: {} is resting".format(self.hFloors[0])
        fin += "\nThe Training Room: {} is training\nThe Library: {} is studying".format(self.hFloors[1],self.hFloors[2])
        return fin
