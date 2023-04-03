print("## Program Python Persegi Deret Angka ##")
print("====================================")
print()

besar_persegi = int(input('Input besar persegi: '))
print()

x = 1
for i in range(1,besar_persegi+1):
    for j in range(1,besar_persegi+1):
        print(x," ", end='')
        x = x + 1
    print()
    
print()

x = 1
for i in range(besar_persegi):
    for j in range(besar_persegi):
        print(f"{x:>3} ", end='')
        x = x + 1
    print()
