class Hero:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.__info = 'Name {} : \n\thealth: {}'.format(self.name, self.__health)

    @property # membuat fungsi berprilaku seperti variable
    def info(self):
        return 'Name {} : \n\thealth: {}'.format(self.name, self.__health)
    
    ''''ARMOR'''
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input
    
    @armor.deleter
    def armor(self):
        print('Hapus Armor')
        self.__armor = None

kirito = Hero('Kirito', 300, 100)

print('Merubah info hero')
print(kirito.info)
kirito.name = 'agung'
print(kirito.info)

print('getter dan setter untuk __armor: ')
print(kirito.armor)
kirito.armor = 50
print(kirito.armor)

print('Delete armor')
del kirito.armor
print(kirito.armor)