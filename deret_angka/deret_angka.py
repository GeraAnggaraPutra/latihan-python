print("## Program Python Menghitung Deret Angka ##")
print("==================================================")

jumlah = int(input('jumlah deret: '))

for i in range(1,jumlah+1):
    print(i, " ", end='')
print()
for i in range(1,jumlah+1):
    print(i*3, " ", end='')
print()
for i in range(1,jumlah+1):
    print(i+5, " ", end='')
print()
for i in range(1,jumlah+1):
    print(i*i, " ", end='') # kuadrat