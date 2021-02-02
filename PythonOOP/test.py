class BangunDatar:
    
    def __init__(self, sisi, panjang, lebar):
        self._sisi = sisi
        self._panjang = panjang
        self._lebar = lebar
    
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

class Persegi(BangunDatar):
    def __init__(self):
        super()._sisi() = 0
        super().sisi() = 0


agung = Persegi()
agung.sisi = 2
print(agung.sisi)