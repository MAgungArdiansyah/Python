class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1
    
    #method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah
    
    # method static (decorator) berlaku untuk object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
kirito = Hero('Kirito')
print(kirito.getJumlah2())
print(kirito.getJumlah2()) #staticmethod
print(kirito.getJumlah3()) #classmethod
