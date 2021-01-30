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


# awal game sao
kirito = Hero('Kirito', 300, 100)

# game berjalan
print(kirito.getName())
        