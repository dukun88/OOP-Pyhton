class Hero:
    __Heroes = 0
    def __init__(self,name,hp,attPow,armor):
        self.__name = name
        self.__hp1 = hp
        self.__attPow1 = attPow
        self.__armor1 = armor
        self.__level = 1
        self.__exp = 0

        self.__hpMax = self.__hp1 * self.__level
        self.__attPow = self.__attPow1 * self.__level
        self.__armor = self.__armor1 * self.__level

        self.__hp = self.__hpMax

        Hero.__Heroes += 1

    @property
    def info(self):
        return "{} Level ({}): \n\tHealthPoint = {}/{}\n\tAttackPower = {}\n\tArmorDefense = {}".format(self.__name,self.__level,self.__hp,self.__hpMax,self.__attPow,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(40*"=")
            print(self.__name, 'Level up')
            print(40*"=")
            self.__level += 1
            self.__exp -= 100

            self.__hpMax = self.__hp1 * self.__level
            self.__attPow = self.__attPow1 * self.__level
            self.__armor = self.__armor1 * self.__level

    def attack(self, enemy):
        print(self.__name + " attacking " + enemy.__name )
        enemy.defending(self, self.__attPow)
        self.gainExp = 50

    def defending(self, enemy, atpowEnemy):
        print(self.__name + " Attacked " + enemy.__name )
        power = atpowEnemy/self.__armor
        print("Attack from " + enemy.__name + ": " + str(power))
        self.__hp -= power
        print("Health point " + self.__name + ": " + str(self.__hp))





maskman = Hero('Maskman',200, 80, 30)
mage = Hero('Mage',180,100,20)

print("\nPHASE 1\n")
print(maskman.info)
print("\n")
maskman.attack(mage)
print("\n")
print(maskman.info)
print("\n")
maskman.attack(mage)
print("\n")
print(maskman.info)
print("\n")
print("\nPHASE 2\n")
print(mage.info)
print("\n")
mage.attack(maskman)
print("\n")
print(mage.info)
print("\n")
mage.attack(maskman)
print("\n")
print(mage.info)
print("\n")


