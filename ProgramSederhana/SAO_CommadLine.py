import time
class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, hp, attcpow, armor): # variable yang bisa di seting
        self.__name = name
        self.__hpBase = hp
        self.__attBase = attcpow
        self.__armorBase = armor
        # varible yang g bisa di seting
        self.__level = 1
        self.__exp = 0
        self.__gold = 0

        self.__hpMax = self.__hpBase * self.__level
        self.__attMax = self.__attBase * self.__level
        self.__armorMax = self.__armorBase * self.__level

        self.__hp = self.__hpMax
        self.__att = self.__attMax
        self.__armor = self.__armorMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return '{} : \n\tLevel  : {}\n\tHealth : {}/{} \n\tAttack : {}\n\tArmor  : {}\n\tGold : {}'.format(self.__name,self.__level, self.__hp, self.__hpMax, self.__att, self.__armor, self.__gold)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print('Level Up!!')
            self.__level += 1
            self.__exp -= 100

    @property
    def gainGold(self):
        pass

    @gainGold.setter
    def gainGold(self, addGold):
        self.__gold += addGold


    def Attack(self, enemy):
        print(self.__name, ' Menyerang ', enemy.__name)
        time.sleep(2) # pause 2 second
        # Hero Attacing the Enemy
        enemy.__hp = enemy.__hp - self.__att 
        print(enemy.__name, ' Menyerang ', self.__name)
        time.sleep(2)
        # enemy counter attack
        self.__hp = self.__hp - enemy.__att 
        print(self.info)
        print(enemy.info)
        time.sleep(1)
        if enemy.__hp == 0:
            print('Anda Menang!!')
            self.gainExp = 150
            self.gainGold = 1000
    


# pembuatan object
kirito = Hero('Kirito', 300, 100, 50)
asuna = Hero('Asuna', 250, 150, 25)
Egil = Hero('Egil', 200, 100, 10)

# main programs
i = 1
while i == 1:
    print('\t\tWelecome To SAO Commadline')
    print('Silahkan Pilih Karaktermu')
    print('''
        1. Kirito
        2. Asuna
        3. Keluar Game
        ''')
    pilihan = int(input('Karakter Pilihan Anda: '))
    if pilihan == 1:
        print(kirito.info)
        print('Anda ingin menggunakan karakter ini?')
        print('1. ya\n2. tidak')
        pilChar = int(input('Masukan Nomor pilihan anda: '))
        if pilChar == 1:
            print('Anda Memilih : Kirito')
            kirito.Attack(Egil)
            kirito.Attack(Egil)
            print(kirito.info)

        else:
            i = 1
    elif pilihan == 2:
        print(asuna.info)
        print('Anda ingin menggunakan karakter ini?')
        print('1. ya\n2. tidak')
        pilChar = int(input('Masukan Nomor pilihan anda: '))
        if pilChar == 1:
            print('Anda Memilih : asuna')
            asuna.Attack(Egil)
            asuna.Attack(Egil)
            print(asuna.info)
    elif pilihan == 3:
        i = 0
    else:
        print('Pilihan yang anda masukan tidak tersedia')
        print('Apakah anda ingin mengulang pemilihan karakter?')
        print('''
            1. Ya
            2. Tidak
            ''')
        pilihan2 = int(input('Silahkan Masukan Nomor Pilihan anda: '))
        if pilihan2 == 1:
            i = 1
        else:
            i = 0

print('Terimakasih telah mencoba program saya')
            