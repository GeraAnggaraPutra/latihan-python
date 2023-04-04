print("## Program Python Mencari Nilai Terkecil ##")
print("==================================================")

n = int(input('Input jumlah element list: '))
print()

print('Input',n,'angka (dipisah dengan enter):')

x = [] # simpan angka ke dalam list
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()

min_num = x[0]
for i in range(1,n):
    if(x[i] < min_num):
        min_num = x[i]

print('Angka terkecil adalah:', min_num)

# menggunakan function min()
x = []
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()
print('Angka terkecil adalah: ',min(x))