print("## Program Python Persegi Angka ##")
print("====================================")
print()

besar_persegi = int(input('Input besar persegi: '))
print()

for i in range(1,besar_persegi+1):
    for j in range(1,besar_persegi+1):
        print(j," ", end='')
    print()
    
print()

for i in range(1,besar_persegi+1):
    for j in range(besar_persegi):
        print(i," ", end='')
    print()