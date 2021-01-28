def name(x):
    print(x)
    return

nama = input('Masukan Nama Anda: ')
name(nama)

'''
by default python is call by references mean
if you 'change' variable it make the data will change to
'''
def  ubah(listSaya):
    listSaya.append([1, 2, 3, 4])
    print('Nilai dalam fungsi {}'.format(listSaya))

listSaya = [10, 20, 30]
ubah(listSaya)
print('Nilai diluar fungsi {}'.format(listSaya))


'''
Call by value, this will not change the variable
if you declare some ne assignment with the same name
that mean you create a local variable
'''
def  ubah2(listSaya):
    listSaya = [1, 2, 3, 4]
    print('Nilai dalam fungsi {}'.format(listSaya))

listSaya = [10, 20, 30]
ubah2(listSaya)
print('Nilai diluar fungsi {}'.format(listSaya))