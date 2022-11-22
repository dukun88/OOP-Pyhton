class Hero:
    def __init__(self,name,hp,atpow,defpow) :
        self.name = name
        self.health = hp
        self.attack = atpow
        self.defense = defpow

    def attacking(self, enemy):
        print(self.name + " attacking " + enemy.name )
        enemy.defending(self, self.attack)

    def defending(self, enemy, atpowEnemy):
        print(self.name + " Attacked " + enemy.name )
        power = atpowEnemy/self.defense
        print("Attack from " + enemy.name + ": " + str(power))
        self.health -= power
        print("Health point " + self.name + ": " + str(self.health))

archer = Hero("Acher",200,80,8)
tank = Hero("Tank",400,10,100)


archer.attacking(tank)
print("\n")
tank.attacking(archer)