from theTavern import *
from hero import *
import time

#taskManager class

class taskManager:

    def __init__(self):
        self.tasks = []

    def addTask(self, task, h):
        self.tasks.append([task,h])

    def delTask(self, h):
        for x in self.tasks:
            if x[1] == h:
                self.tasks.remove(x)

    def clearHeroTasks(self, tav):
        self.tasks.clear()
    

    def do(self, tav):
        if len(self.tasks) != 0:
            for x in self.tasks:
                if x[0] == "lib":
                    x[1].ipUp(1)
                elif x[0] == "train":
                    x[1].spUp(1)
                elif x[0] == "rest":
                    x[1].hpDn(-1)
        tav.gold += tav.lvl*3
        time.sleep(1)

    def __str__(self):
        return str(self.tasks)
