def persegi():
    print('Perhitungan Luas Persegi')
    x = float(input('Masukan Sisi: '))
    luasPersegi = x**2
    print('Luas Persegi : ',luasPersegi)
    return

def segitiga():
    print('Perhitungan Luas Segitiga')
    x = float(input('Masukan Alas: '))
    y = float(input('Masukan Tinggi: '))
    luasSegitiga = (x*y)/2
    print('Luas Segitiga: ',luasSegitiga)
    return

def PersegiPanjang():
    print('Perhitungan Luas Persegi Panjang')
    x = float(input('Masukan Panjang: '))
    y = float(input('Masukan Lebar'))
    luasPersegiP = x*y
    print('Luas Persegi Panjang: ',luasPersegiP)
    return
i = 1
while i == 1:
    print('Program Perhitungan Luas Bangun Datar')
    print('Silahkan Pilih Bangun Datar')
    print('''
    1. Persegi
    2. Segitiga
    3. Persegi Panjang
    4. Keluar Program
    ''')
    pilihan = int(input('Silahkan Masukan Pilihan Anda: '))
    if pilihan == 1:
        persegi()
        print('''
        Apakah anda ingin mencoba kembali?
        1. Iya
        2. Tidak
        ''')
        i = int(input('Masukan Nomor Pilihan Anda: '))
    elif pilihan == 2:
        segitiga()
        print('''
        Apakah anda ingin mencoba kembali?
        1. Iya
        2. Tidak
        ''')
        i = int(input('Masukan Nomor Pilihan Anda: '))
    elif pilihan == 3:
        PersegiPanjang()
        print('''
        Apakah anda ingin mencoba kembali?
        1. Iya
        2. Tidak
        ''')
        i = int(input('Masukan Nomor Pilihan Anda: '))
    elif pilihan == 4:
        i = 0
    else:
        print('Pilihan tidak tersedia!!')
        print('''
        Apakah anda ingin mencoba kembali?
        1. Iya
        2. Tidak
        ''')
        i = int(input('Masukan Nomor Pilihan Anda: '))
print('Terimkasih telah mencoba program yang saya buat')