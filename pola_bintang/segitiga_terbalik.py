print("## Program Python Segitiga Terbalik Bintang ##")
print("====================================")
print()

tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()

for i in range(tinggi_segitiga):
    print(' *' * (tinggi_segitiga-i))

print()

for i in range(tinggi_segitiga):
    for j in range(tinggi_segitiga-i):
        print(' *', end='')
    print()