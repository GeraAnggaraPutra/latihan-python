print("## Program Python Mencari Nilai Rata - rata ##")
print("==================================================")

n = int(input('Input jumlah element list: '))
print()

print('Input',n,'angka (dipisah dengan enter):')

x = [] # simpan angka ke dalam list
for i in range(n):
    print('Angka ke-',i+1,': ',end='')
    x.append(int(input()))

print()

rata2 = round(sum(x)/n,2)

print('Nilai rata-rata dari',n,'angka adalah', rata2)
