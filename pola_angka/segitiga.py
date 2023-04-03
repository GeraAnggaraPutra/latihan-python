print("## Program Python Segitiga Angka ##")
print("====================================")
print()

tinggi_segitiga = int(input('Input tinggi segitiga: '))
print()

for i in range(tinggi_segitiga+1):
    for j in range(1,i+1):
        print(j,' ', end='')
    print()
    
print()

for i in range(tinggi_segitiga+1):
    for j in range(i):
        print(i,' ', end='')
    print()