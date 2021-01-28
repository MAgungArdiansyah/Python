class Hero: # membuat kelas
    
    def __init__(self, InputName, InputHealth, InputPower, InputArmor):
        self.name = InputName
        self.Hp = InputHealth
        self.AttPow = InputPower
        self.Amr = InputArmor


hero1 = Hero('Kirito', 300, 500, 250)
hero2 = Hero('Asuna', 280, 700, 150)
hero3 = Hero('Administrator', 1000, 500, 400)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
