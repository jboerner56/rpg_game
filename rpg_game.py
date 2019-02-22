# # create character class
class Character():
    def __init__(self, health, power, name):
        self.health = health
        self.name = name
        self.power = power
    # put code shared by each subclass so it does not have to be written twice.
    def alive(self):
        return self.health > 0
    def attack(self, enemy):
        self.health -= enemy.power
        print("%s attacked you and caused %d damage" % (enemy.name, enemy.power))
    def print_status(self):

        if self.health <= 0:
            return "The %s is dead" % self.name 
        elif self.health > 0:
            return "%s is still alive" % self.name
        else:
            return "still alive"

# create class for hero
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.name = "Hero"
        # sets up attack on the goblin
    # def attack(self, enemy):
    #         # Hero attacks goblin
    #     enemy.health -= self.power
    #     print("You do %d damage to the goblin." % self.power)
    # def alive(self):
    #     return self.health > 0
    
    # def print_status(self):
    #     if self.health <= 0:
    #         return "You are dead."
    #     else:
    #         return "your alive"
class Goblin(Character):
    def __init__(self):
        self.power = 2
        self.health = 6
        self.name = "Goblin"
# create function/method for when goblin attacks hero
    # def attack(self, enemy):
    #         # Goblin attacks hero
    #     enemy.attack -= self.health
    #     print("The goblin does %d damage to you." % self.power)
    # def alive(self):
    #     return self.health > 0
    # def print_status(self):
    #     if self.health <= 0:
    #         return "The goblin is dead."
    #     else:
    #         return "still alive"
# instance for hero attacking goblin and goblin attacking hero
goodguy = Hero()
badguy = Goblin()
print(goodguy.print_status())
# class Zombie():
#     def __init__(self):
#         self.health = 100000
#         self.power = 10


while goodguy.alive() == True and badguy.alive() == True:
    print("You have %d health and %d power." % (goodguy.health, goodguy.power))
    print("The goblin has %d health and %d power." % (badguy.health, badguy.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()
    if user_input == "1":
    # Hero attacks goblin
        badguy.health -= goodguy.power
        print("You do %d damage to the goblin." % goodguy.power)
        badguy.print_status()
    elif user_input == "2":
        pass
    elif user_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)

    if badguy.health > 0:
        # Goblin attacks hero
        # goodguy.health -= badguy.health
        # print("The goblin does %d damage to you." % badguy.health)
        goodguy.print_status()

