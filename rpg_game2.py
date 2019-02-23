"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time
class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        # enemy.print_status()
        
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def attack(self, enemy):
        print("%s has %d health and %d power." % (enemy.name, enemy.health, enemy.power))
        # random integer
        if random.randint(1,5) == 5:
            enemy.receive_damage((self.power * 2))
        else:
            enemy.receive_damage(self.power)


    def restore(self):
        self.health = 10
        print("%s heath is restored to %d!" % (self.name, self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        if self.health <= 0:
            hero.coins +=5


class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        if self.health <= 0:
            hero.coins += 6


    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power
class Medic(Character):
    def __init__(self):
        self.name = "medic"
        self.health = 10
        self.power = 1
        if random.randint(1,5) == 5:
            self.health == self.health + 5

class Shadow(Character):
    def __init__(self):
        self.name = "Shadow"
        self.health = 1
        self.power = 7
    def receive_damage(self, damage):
        print("you are attacking the shadow")
        if random.randint(1,10) < 2:
            self.health -= damage
            print("little better you hit")
        else:
            print("you suck you missed")
        # self.receive_damage = enemies[3].power
        # else:
        #     self.receive_damage = 0
class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 10
        self.power = 5
        if self.health <= 0:
            self.health + 10
class God(Character):
    def __init__(self):
        self.name = "God"
        self.health = 20
        self.power = 10
        if self.health <= 10:
            print(self.health)
            self.health += 10
            print("Gods health was replenished by 10, He can't die.")
class Bob_Ross(Character):
    def __init__(self):
        self.name = "Bob Ross"
        self.health = 10
        self.power = 10
        if self.health <= 5:
            self.health += 5
            print(self.health)


    
class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        # print("Who do you want the hero to face")

        # print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            
            time.sleep(1.0)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight")
            print("2. do nothing")
            print("3. flee")
            print("4. Enter store ",)
            user_input1 = int(input())
            if user_input1 == 1:
                
                print("You chose fight. Who do you want to fight")
                # list of print statements of each enemy option
                print("1. Fight Goblin")
                print("2. Fight Wizard")
                print("3. Fight Medic")
                print("4. Fight Shadow")
                print("5. Fight Zombie")
                print("6. Fight God. Not Recommended!")
                print("7. Fight Bob Ross. Also not recommended!")
                user_input2 = int(input())
                # print(enemies[0])
                if user_input2 == 1:
                    hero.attack(enemies[0])
                elif user_input2 == 2:
                    hero.attack(enemies[1])
                elif user_input2 == 3:
                    hero.attack(enemies[2])
                elif user_input2 == 4:
                    hero.attack(enemies[3])
                elif user_input2 == 5:
                    hero.attack(enemies[4])
                elif user_input2 == 6:
                    hero.attack(enemies[5])
                elif user_input2 == 7:
                    hero.attack(enemies[6])
                    
            elif user_input1 == 2:
                enemy.attack(hero)
            elif user_input1 == 3:
                print("Goodbye.")
                exit(0)
                # for accessing the store
            elif user_input1 == 4:
                shopping_engine.do_shopping()
            else:
                print("Invalid input %r" % user_input1)
                continue
            
        if hero.alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))
class SuperTonic(object):
    cost = 15
    name = "supertonic"
    def apply(self, hero):
        hero.health += 10
        print("%s's health increased to %d" % (hero.name, hero.power))
class Armor(object):
    cost = 5
    name = "Armor"
    def apply(self, hero):
        enemy.power -= 2
class Evade(object):
    cost = 5
    name = "evade"
    def apply(self, hero):
        if evade_points == 2 and random.randint(1,10) == 10: 
            enemy.power = 0
class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, SuperTonic, Armor]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
# add character classes to enemies for each enemy created.
# enemies = [Wizard(), Medic()]
# enemies = [God()]
enemies = [Goblin(), Wizard(), Medic(), Shadow(),Zombie(), God(), Bob_Ross()]
battle_engine = Battle()
shopping_engine = Store()
evade_points = Evade()
for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
