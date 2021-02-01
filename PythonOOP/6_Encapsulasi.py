'''
Aturan Encapsulasi
1. Buats semua variable private
2. Gunakan metode getter and setter
'''
class Hero:

    def __init__(self, name, health, attcpow):
        self.__Name = name
        self.__Hp = health
        self.__Att = attcpow
    
    # getter
    def getName(self):
        return self.__Name
    
    def getHealth(self):
        return self.__Hp

    # Setter
    def setAtt(self, NewAtt):
        self.__Att = NewAtt
    
    def diserang(self, AttPow):
        self.__Hp -= AttPow


# awal game sao
kirito =   Hero('Kirito', 300, 100)

# game berjalan
print(kirito.getName())
print(kirito.getHealth())
kirito.diserang(100)
print(kirito.getHealth())

        