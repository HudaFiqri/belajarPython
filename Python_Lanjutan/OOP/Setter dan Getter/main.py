'''
encapsulasi menggunakan setter dan getter

sumber referensi: - pintaar module
                  - https://www.geeksforgeeks.org/getter-and-setter-in-python/
ditulis pada: 07-03-2021
'''
class Hero:

    def __init__(self, Name, Health, Power, Armor):
        self.__Hero_Name = Name
        self.__Hero_Health = Health
        self.__Hero_Power = Power
        self.__Hero_Armor = Armor

    # getter
    def HeroInfo(self):
        return self.__Hero_Name, self.__Hero_Health, self.__Hero_Power, self.__Hero_Armor

    # setter
    def HeroBuff(self):
        self.__Hero_Health += 500
        self.__Hero_Power += 100
        self.__Hero_Armor += 100

Hero_Module = Hero(Name='Paladin', Health=1000, Power=100, Armor=300)

print('hero before buffing')
print(Hero_Module.HeroInfo())


print('hero after buffing')
Hero_Module.HeroBuff()
print(Hero_Module.HeroInfo())