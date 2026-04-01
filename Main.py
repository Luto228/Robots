import random

import time

RamLvl = random.randint(10, 100)

RamLvl2 = random.randint(10, 100)

FulRandom = []


class Robot:
    name = None

    lvl = None

    attack = None

    def __init__(self, name, lvl, health):
        self.name = name

        self.lvl = lvl

        self.health = health

    def Print(self):
        print(f'{self.name} lvl: {self.lvl}')


class AssasinRobot(Robot):

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)

        self.lvl = lvl * 1.7

        self.health = health / 2

        print(f'Роботу {self.name}, выпал класс Ассасина!')


class TitanRobot(Robot):

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)

        self.lvl = lvl / 2.01

        self.health = health * 2.3

        print(f'Роботу {self.name}, выпал класс Титана!')


class FocusRobot(Robot):

    def PlusHealth(self):
        self.health += 40

        print('И у него +40 хп!')

    def MinusHealth(self):
        self.health -= 40

        print('Но у него минус 40 хп!')

    def PlusAttack(self):
        self.lvl = self.lvl * 2

        print('И у него в 2 раза больше урона!')

    def MinusAttack(self):
        self.lvl = self.lvl / 2

        print('И у него в 2 раза меньше урона!')

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)

        if self.health == 100:
            self.health += 40

        Health = [self.PlusHealth, self.MinusHealth]

        Attack = [self.PlusAttack, self.MinusAttack]

        RamHe = random.choice(Health)

        RamAt = random.choice(Attack)

        RamHe()

        RamAt()

        print(f'Роботу {self.name}, выпал класс Фокусника!')


RobotsClasses = [

    FocusRobot,

    TitanRobot,

    AssasinRobot

]

RandomName = ['Alex', 'Glorbo', 'Monster', 'King', 'SuperMan', 'Soloma', 'Master', 'Robo', 'XXX', 'IDK', 'Burher']

RamName, RamName2 = random.sample(RandomName, 2)

RamClasses = random.choice(RobotsClasses)

RamClasses2 = random.choice(RobotsClasses)

Robot1 = RamClasses(RamName, RamLvl, 100)

Robot2 = RamClasses2(RamName2, RamLvl2, 100)

while True:

    time.sleep(1)

    if Robot2.health > 0:
        Robot2.health -= Robot1.lvl

        print(f'{Robot1.name} нанес атаку роботу {Robot2.name}, у {Robot2.name} \n осталось {int(Robot2.health)} !')

    if Robot2.health <= 0:
        print(f'Битва закончена! У {Robot2.name} 0 хп!')

        break

    time.sleep(1)

    if Robot1.health > 0:
        Robot1.health -= Robot2.lvl

        print(f'{Robot2.name} нанес атаку роботу {Robot1.name}, у {Robot1.name} \n осталось {int(Robot1.health)} !')

    if Robot1.health <= 0:
        print(f'Битва закончена! У {Robot1.name} 0 хп!')

        break