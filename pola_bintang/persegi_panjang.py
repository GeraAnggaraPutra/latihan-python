print("## Program Python Persegi Panjang Bintang ##")
print("============================================")
print()

tinggi = int(input('Input tinggi: '))
lebar = int(input('Input lebar: '))
print()

for i in range(tinggi):
    print(' *' * lebar)

print()

for i in range(tinggi):
    for j in range(lebar):
        print(' *', end='')
    print()