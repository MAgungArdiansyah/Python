print(
    '''Jumlah 4 buah bilangan kuadrat pertama adalah 30 (30=1+4+9+16), 
    berapakah jumlah 1000 bilangan kuadrat pertama?'''
    )
#test 1
d = 0
for a in range (0, 1001):
    d += a**2
print(d)

#test 2
f = 0
for i in range (0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        f += i
print(f)

#test 3
a = 1
b = 2
c = 0
g = 0
for r in range(0, 10):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
#    if r % 2 != 0:
#        print(a, end=' ')
print('')
print (a)