from random import randint

class Hero:
    def __init__(self, n, t, lvl = 1):
        self.number = n
        self.team = t
        self.lvl = lvl
    def levelUp(self):
        self.lvl += 1
        print(f"Уровень повышен! Текущий уровень героя {self.number}: {self.lvl}\n")
        
class Soldier:
    def __init__(self, n, t):
            self.number = n
            self.team = t
    def follow(self, target):
         print(f"{self.number} следует за {target.number}\n")


heroAllience = Hero("Герой Альянса", "Альянс")
heroUndead = Hero("Герой Нежити", "Нежить")

squad_alliance = []
squad_undead = []

for i in range(randint(1, 5)):
        squad_alliance.append(Soldier("Паладин " + f"{i + 1}", "Альянс"))       
for i in range(randint(1, 5)):
        squad_undead.append(Soldier("Гуль " + f"{i + 1}", "Нежить"))
        
print(f"Армия Альянса насчитывает {len(squad_alliance)} отважных паладинов\n")

print(f"Армия Нежити насчитывает {len(squad_undead)} мерзких гулей\n")

if len(squad_alliance) > len(squad_undead):
    heroAllience.levelUp()
else:
    heroUndead.levelUp()

squad_alliance[randint(0, len(squad_alliance) - 1)].follow(heroAllience)
