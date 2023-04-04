print("## Program Python Penjumlahan List / Array ##")
print("==================================================")

n = int(input('Input jumlah element list: '))
print()

print('Input',n,'angka (dipisah dengan enter):')

y = 0 # simpan angka ke dalam list
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x = int(input())
    y = y + x

print('Total penjumlahan dari',n,'angka adalah:', y)

print()
## menggunakan fungsi sum()
x = []
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

total = sum(x)
print('Total penjumlahan dari',n,'angka adalah:', total)
