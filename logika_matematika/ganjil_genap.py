print("## Program Python Menentukan Ganjil-Genap ##")
print("==================================================")

x = int(input('Input angka bulat: '))

genap =  True
if(x % 2 == 0):
    genap = True
else:
    genap = False

if(genap):
    print(x, 'adalah bilangan genap')
else:
    print(x, 'adalah bilangan ganjil')