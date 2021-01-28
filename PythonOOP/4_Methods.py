class Hero:
    #class variable
    JumlahHero = 0

    def __init__(self, InputName, InputHealth, InputPower, InputArmor):
        # intance / object variable
       self.name = InputName
       self.Hp = InputHealth
       self.AttPow = InputPower
       self.Amr = InputArmor
       Hero.JumlahHero += 1

    
    # fungsi tanpa nilai balik + argumen
    def perkenalan(self):
        print('Namaku adalah ', self.name)
    
    # method dengan return
    def healthUp(self, up):
        self.Hp += up
    
    # method dengan return
    def getHp(self):
        return self.Hp

hero1 = Hero('Kirito', 300, 500, 250)
hero2 = Hero('Asuna', 280, 700, 150)
hero3 = Hero('Administrator', 1000, 500, 400)

print(hero1.perkenalan())
hero1.healthUp(10)
print(hero1.getHp())