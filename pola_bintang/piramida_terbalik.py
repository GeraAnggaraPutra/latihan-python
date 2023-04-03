print("## Program Python Piramida Terbalik Bintang ##")
print("====================================")
print()

tinggi_piramida = int(input('Input tinggi piramida: '))
print()

for i in range(tinggi_piramida):
    print(' ' * (i+1),end='')
    print('* ' * (tinggi_piramida-i))

print()

for i in range(tinggi_piramida):
    for j in range(i+1):
        print(' ', end='')
    for k in range(tinggi_piramida-i):
        print('* ',end='')
    print()