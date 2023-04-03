print("## Program Python Menghitung Deret Angka Faktorial ##")
print("==================================================")

angka = int(input('Input angka: '))
print(angka, '! = ', end="")

hasil = 1
for i in range(1,angka+1):
    hasil = hasil * i
    print(i, end='')
    if(i != angka):
        print(' *' , end="")

print(' =', hasil)