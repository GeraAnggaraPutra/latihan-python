print("## Program Python Pencarian List / Array ##")
print("==================================================")

n = int(input('Input jumlah element list: '))
print()

print('Input',n,'angka (dipisah dengan enter):')

x = [] # simpan angka ke dalam list
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()

cari = int(input('Input angka yang akan dicari: '))

for i in range(n):
    if(x[i] == cari):
        print('Angka ditemukan pada urutan ke', i+1)
        break

if(i+1 > n):
    print('Angka tidak ditemukan')

