class BangunDatar:
    _sisi = 0
    _panjang = 0
    _lebar = 0
    _alas = 0
    _tinggi = 0

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

    # Alas
    @property
    def alas(self):
        pass
    
    @alas.getter
    def alas(self):
        return self._alas
    
    @alas.setter
    def alas(self, input):
        self._alas = input
    
    # tinggi
    @property
    def tinggi(self):
        pass
    
    @tinggi.getter
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, input):
        self._tinggi = input

class Persegi(BangunDatar):
    def __init__(self, sisi):
        super()._sisi()
        super().sisi()

    def luas(self):
        print('menghitung luas persegi')
        self._sisi = float(input('Masukan Sisi : '))
        hasil = self._sisi * 2
        return hasil

agung = Persegi()
agung.luas()

    