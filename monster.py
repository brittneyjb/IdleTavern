#Monster Class

class Monster:

    def __init__(self,n,l):
        self.name = n
        self.lvl = l
        self.hp = self.lvl**2*25
        self.award = self.lvl**3*100

    def __str__(self):
        fin = self.name
        fin += "\nInt: "+str(self.getInt())
        fin += "\nStrength: "+str(self.getStr())
        fin += "\nHealth: "+str(self.hp)
        fin += "\nWinAward: "+str(self.award)+" Gold"
        return fin

    def getName(self):
        return self.name

    def getLvl(self):
        return self.lvl

    def getInt(self):
        return self.lvl**2*10-2

    def getStr(self):
        return self.lvl**2*10+2

    def getHP(self):
        return self.hp

    def getGold(self):
        return self.award

    def decHP(self,hit):
        self.hp -= hit
