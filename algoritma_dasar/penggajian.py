print("## Program Python Menghitung Gaji Karyawan ##")
print("==================================================")

nama = input('Nama karyawan: ')
golongan = input('Golongan: ')
jam = int(input('Jumlah jam kerja: '))

if(golongan == 'A'):
    upah = 5000 * jam
elif(golongan == 'B'):
    upah = 7000 * jam
elif(golongan == 'C'):
    upah = 8000 * jam
elif(golongan == 'D'):
    upah = 10000 * jam
else:
    upah = 0

if(jam >= 48):
    lembur = (jam - 48) * 4000
else:
    lembur = 0

gaji = upah + lembur

print(nama,' menerima upah Rp.',gaji,'per minggu')