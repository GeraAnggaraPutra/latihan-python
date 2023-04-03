print("## Program Python Persegi Bintang ##")
print("====================================")
print()

besar_persegi = int(input('Input besar persegi: '))
print()

for i in range(besar_persegi):
    print(' *' * besar_persegi)

print()

for i in range(besar_persegi):
    for j in range(besar_persegi):
        print(' *', end='')
    print()