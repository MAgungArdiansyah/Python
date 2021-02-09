# method resolution order = mengurutkan instruksi / fungsi objeck
# berdasarkan urutan kelas inheritance misal
# object(a,b) maka fungsi dengan nama yang sama akan dieksekusi
# dari kelas a terlebih dahulu, bila fungsi yang namanya sama
# ada dalam kelas C maka fungsi tersebut yang akan dieksekusi

class A:
    def show(self):
        print('ini adalah show A')

class B:
    def show(self):
        print('ini adalah show B')

class C(A,B):
    pass

objek = C()
print(objek.show())
