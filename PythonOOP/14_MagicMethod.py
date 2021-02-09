class Mangga:

    # Magic Method ditandai dengan __X__
    
    def __init__(self, nama, jumlah): # fungsi yang pertamakai dieksekusi
        self.nama = nama
        self.jumlah = jumlah
    
    def __repr__(self): # fungsi yang digunakan untuk membantu debunging
        return 'Debug - Mangga: {} dengan jumlah {}'.format(self.nama, self.jumlah)
    
    def __str__(self):
        return 'Mangga: {} dengan jumlah {}'.format(self.nama, self.jumlah)

    def __add__(self, objek): # fungsi yang digunakan dalam tahap produksi program
        return self.jumlah + objek.jumlah
    
    def __dict__(self):
        return 'objek ini mempunyai nama dan jumlah'

belanja1 = Mangga('arumanis', 10)
belanja2 = Mangga('mana lagi', 30)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)