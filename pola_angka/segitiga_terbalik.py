print("## Program Python Segitiga Terbalik Angka ##")
print("====================================")
print()

tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()

for i in range(tinggi_segitiga):
    for j in range(tinggi_segitiga-i):
        print(j+1,' ', end='')
    print()

print()

for i in range(tinggi_segitiga):
    for j in range(tinggi_segitiga-i):
        print(i+1,' ', end='')
    print()