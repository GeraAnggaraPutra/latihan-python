print("## Program Python Segitiga Deret Angka ##")
print("====================================")
print()

tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()

for i in range(tinggi_segitiga+1):
    for j in range(1,i+1):
        print(j,' ', end='')
    print()
    
print()

k = 1
for i in range(tinggi_segitiga+1):
    for j in range(i):
        print(f'{k:>2} ', end='')
        k = k + 1
    print()