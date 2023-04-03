print("## Program Python Menghitung Deret Angka Genap ##")
print("==================================================")

jumlah = int(input('jumlah deret: '))

for i in range(1,jumlah+1):
    print(i*2, " ", end='')

print()
print("## Program Python Menghitung Deret Angka Ganjil ##")
print("==================================================")

jumlah = int(input('jumlah deret: '))

for i in range(1,jumlah+1):
    print((i*2)-1, " ", end='')

print()
print("## Program Python Menghitung Deret Angka Genap ##")
print("==================================================")

awal = int(input('input angka awal: '))
akhir = int(input('input angka akhir: '))

for i in range(awal,akhir+1):
    if(i % 2 == 0):
        print(i, end=" ")

print()
print("## Program Python Menghitung Deret Angka Ganjil ##")
print("==================================================")

awal = int(input('input angka awal: '))
akhir = int(input('input angka akhir: '))

for i in range(awal,akhir+1):
    if(i % 2 != 0):
        print(i, end=" ")