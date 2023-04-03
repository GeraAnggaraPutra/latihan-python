print("## Program Python Konversi Biner ke Desimal ##")
print("==================================================")

biner = input('Input angka biner: ') #cara cepat
angka_desimal = int(biner,2) #cara cepat
print(angka_desimal) #cara cepat


biner = int(input('Input angka biner: '))
desimal = 0
i = 1
while (biner != 0):
    digit = biner % 10
    desimal = desimal + (digit*i)
    i = i * 2
    biner = biner // 10
    
print('Angka desimalnya adalah: ',desimal, end='')