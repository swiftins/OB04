"""Есть класс Fighter, представляющий бойца.
Есть класс Monster, представляющий монстра.
Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
Шаг 1: Создайте абстрактный класс для оружия
Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
Шаг 2: Реализуйте конкретные типы оружия
Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
Шаг 3: Модифицируйте класс Fighter
Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
Шаг 4: Реализация боя
Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия."""

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None 

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self, target):
        if not self.weapon:
            print(f"{self.name} не может атаковать без оружия!")
            return
        self.weapon.attack()
        target.take_damage(10)  

class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"Монстр получил {damage} урона. Осталось здоровья: {self.health}")
        else:
            print("Монстр побежден!")

def main():
    
    fighter = Fighter("Боец")
    monster1 = Monster(health=10)

    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack(monster1)

    monster2 = Monster(health=10)

    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack(monster2)

if __name__ == "__main__":
    main()
