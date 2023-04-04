print("## Program Python Mencari Nilai Terbesar ##")
print("==================================================")

n = int(input('Input jumlah element list: '))
print()

print('Input',n,'angka (dipisah dengan enter):')

x = [] # simpan angka ke dalam list
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()

max_num = x[0]
for i in range(1,n):
    if(x[i] > max_num):
        max_num = x[i]

print('Angka terbesar adalah:', max_num)

# menggunakan function max()
x = []
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()
print('Angka terbesar adalah: ',max(x))