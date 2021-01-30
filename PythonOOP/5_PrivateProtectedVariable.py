class Hero:
    # class variable
    jumlahHero = 0

    # class private variable
    __privateJumlah = 0
    # class protected variable
    _protectedJumah = 0


    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable intance private
        self.__private = 'private'

        # variable intance protected
        self._protected = 'protected'

# membuat object
lina = Hero('Lina', 100)
print(lina.__dict__)
print(lina.health)
print('')
# mencoba memanggil variable private
#print(lina.private)

# memanggil variable protected
print('')
print(lina._protected)
lina._protected = 'siwah'
print(lina._protected)