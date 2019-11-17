#Hero Class
import random

class Hero:

    
    def setWiz(self):
        self.sp = random.randint(1,10)
        self.ip = random.randint(5,15)
        self.hp = random.randint(5,10)*5

    def setWar(self):
        self.sp = random.randint(5,15)
        self.ip = random.randint(1,10)
        self.hp = random.randint(8,14)*5

        
    def __init__(self, t):
        self.clss = t
        self.sp = 0
        self.ip = 0
        self.name = " "
        self.lvl = 1
        self.hp = 0
        self.exp = 0
        self.loc = "inn"
        if self.clss == "wizard":
            self.setWiz()
        if self.clss == "warrior":
            self.setWar()
        self.hpMax = self.hp


    def __str__(self):
        fin = "The "+self.clss+", "+self.name+"\n"
        fin += "Level: "+str(self.lvl)+"\n"
        fin += "Exp: "+str(self.exp)+"\n"
        fin += "HealthPoints: "+str(self.hp)+"/"+str(self.hpMax)+"\n"
        fin += "Int: "+str(self.ip)+"\n"
        fin += "Str: "+str(self.sp)+"\n"
        return fin



    def setName(self, n):
        self.name = n

    def setLoc(self, f):
        self.loc = f
        
    def hpDn(self, p):
        self.hp -= p
        if self.hp>self.hpMax:
            self.hp = self.hpMax

    def ipUp(self, p):
        self.ip += p;

    def spUp(self, p):
        self.sp += p

    def expUp(self, p):
        self.exp += p
        self.checkLvl()

    def lvlUp(self):
        self.ip += self.ip*0.45
        self.ip = self.ip//1
        self.sp += self.sp*0.45
        self.sp = self.sp//1
        self.hp += self.hp*0.30
        self.hp = self.hp//1
        self.hpMax = self.hp
        self.lvl += 1

    def lvlExp(self, l):
        l = 2**(l)
        return l*10

    def checkLvl(self):
        while self.exp >= self.lvlExp(self.lvl+1):
            self.lvlUp()

            
    def getName(self):
        if self.name == " ":
            if self.clss == "wizard":
                return "Wizard"
            else:
                return "Warrior"
        nm =self.name+", "
        if self.clss == "wizard":
            return nm+"the Mystical Wizard"
        if self.clss == "warrior":
            return nm+"the Powerful Warrior"

    def getLvl(self):
        return self.lvl
    def getHP(self):
        return self.hp
    def getStr(self):
        return self.sp
    def getInt(self):
        return self.ip
    def getExp(self):
        return self.exp
    def getClass(self):
        return self.clss
    def getLoc(self):
        return self.loc
    
