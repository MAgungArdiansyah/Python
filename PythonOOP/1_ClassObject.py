# version 1
class kalkulator:
    # belajar OOP pertama python euy mangat bro wkwkwk
    a = 123

    def test(self):
        return 'hello world'

print(kalkulator.a)
print(kalkulator.test)
kalkulator.a = 456
print(kalkulator.a)

# membuat object
k = kalkulator()
print(k.test())

class kalkulator2:
    # contoh kelas kalkulator sederhana
    def f(self):
        return 'hello world'
    
    def __init__(self, i=123):
        self.i = i
    
k2 = kalkulator2()
print(k2.i)

# version 2
class Hero: # membuat kelas
    pass


hero1 = Hero() # membuat object
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Kirito'
hero1.health = 300

hero2.name = 'Asuna'
hero2.health = 280

hero3.name = 'Adiministrator'
hero3.health = 1000

print(hero1.name)


