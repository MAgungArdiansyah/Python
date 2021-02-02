class BangunDatar:
    
    def __init__(self, x, y, z):
        self._sisi = x
        self._panjang = y
        self._lebar = z
    
    # Sisi
    @property
    def sisi(self):
        pass
    
    @sisi.getter
    def sisi(self):
        return self._sisi
    
    @sisi.setter
    def sisi(self, input):
        self._sisi = input
    
    # Panjang
    @property
    def panjang(self):
        pass
    
    @panjang.getter
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, input):
        self._panjang = input
    
    # Lebar
    @property
    def lebar(self):
        pass
    
    @lebar.getter
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, input):
        self._lebar = input

class Kotak(BangunDatar):
    
    def Persegi(self):
        print('Perhitungan Luas & Keliling Persegi')
        self.sisi = int(input('Masukan Nilai Sisi: '))
        luas = self.sisi * self.sisi
        Keliling = self.sisi * 4
        print('Luas Persegi = ', luas)
        print('Keliling Persegi = ', Keliling)
    
    def PersegiPanjang(self):
        print('Perhitungan Luas & Keliling Persegi Panjang')
        self.panjang = int(input('Masukan Nilai Panjang: '))
        self.lebar = int(input('Masukan Nilai Lebar: '))
        luas = self.lebar * self.panjang
        Keliling = (2 * self.panjang) + (2 * self.lebar)
        print('Luas Persegi Panjang = ', luas)
        print('Keliling Persegi Panjang = ', Keliling)



persegi = Kotak(0,0,0)
persegi.Persegi()
persegi.PersegiPanjang()