import random

import time

RamLvl = random.randint(10, 100)

RamLvl2 = random.randint(10, 100)

FulRandom = []


class Robot:
    def __init__(self, name, lvl, health):
        self.name = name

        self.lvl = lvl

        self.health = health

    def Print(self):
        print(f'{self.name} lvl: {self.lvl}')
    
    def attack(self, other):
        other.health -= self.lvl
        print(f'{self.name} нанес атаку роботу {other.name}, у {other.name} \n осталось {int(other.health)} !')
    
    def loser(self, other):
        print(f'Битва окончена! У {self.name} 0 ХП! {other.name} выиграл!')


class AssasinRobot(Robot):

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)

        self.lvl = lvl * 1.7

        self.health = health // 2

        print(f'Роботу {self.name}, выпал класс Ассасина! ')


class TitanRobot(Robot):

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)

        self.lvl = lvl // 2.01

        self.health = health * 2.3

        print(f'Роботу {self.name}, выпал класс Титана!')


class FocusRobot(Robot):

    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)
        print(f'Роботу {self.name}, выпал класс Фокусника!')

        if self.health == 100:
            self.health += 40

        Health = [self.PlusHealth, self.MinusHealth]

        Attack = [self.PlusAttack, self.MinusAttack]

        RamHe = random.choice(Health)

        RamAt = random.choice(Attack)

        RamHe()

        RamAt()

    
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
        self.lvl = self.lvl // 2

        print('И у него в 2 раза меньше урона!')


class Vampir(Robot):
    def __init__(self, name, lvl, health):
        super().__init__(name, lvl, health)
        print(f'{self.name} выпад класс Вампира!')
    def attack(self, other):
        Steal = random.choice([True, False])
        other.health -= self.lvl
        if Steal:
            self.health += self.lvl // 2
            print(f'{self.name} нанес удар в {other.name} нанеся {self.lvl} и украв {self.lvl // 2} \n у {self.name} {self.health} ХП!')
        else:
            print(f'{self.name} нанес атаку роботу {other.name}!')
        
        print(f'У {other.name} осталось {other.health}')

RobotsClasses = [

    FocusRobot,

    TitanRobot,

    AssasinRobot,

    Vampir
]

RandomName = ['Alex', 'Glorbo', 'Monster', 'King', 'SuperMan', 'Soloma', 'Master', 'Robo', 'XXX', 'IDK', 'Burher']

RamName, RamName2 = random.sample(RandomName, 2)

RamClasses = random.choice(RobotsClasses)

RamClasses2 = random.choice(RobotsClasses)

Robot1 = RamClasses(RamName, RamLvl, 100)

Robot2 = RamClasses2(RamName2, RamLvl2, 100)

while True:

    time.sleep(1)

    if Robot1.health > 0:
       Robot1.attack(Robot2)

    if Robot1.health <= 0:
        Robot1.loser(Robot2)
        break

    time.sleep(1)

    if Robot2.health > 0:
        Robot2.attack(Robot1)

    if Robot2.health <= 0:
        Robot2.loser(Robot1)
        break