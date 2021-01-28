class Hero:
    def __init__(self, name, hp, attcpow, armor):
        self.Name = name
        self.Hp = hp
        self.AttPow = attcpow
        self.Armor = armor
    
    def serang(self,lawan):
        lawan.Hp = lawan.Hp - (self.AttPow - (self.Armor*0.5))
        print(self.Name,'menyerang',lawan.Name)
        print(lawan.Name,'HP tersisa: ', lawan.Hp)
        return 'ahn..!!'
    
    def diserahg
    

kirito = Hero('Kirito', 300, 100, 50)
asuna = Hero('Asuna', 250, 150, 25)

print(kirito.serang(asuna))
    