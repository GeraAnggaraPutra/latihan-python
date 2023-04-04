print("## Program Python Kalkulator Sederhana ##")
print("==================================================")
print()

print('#  Operasi')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Modulus')

operasi = int(input('Input pilihan operasi: '))
if operasi > 5:
    print('operasi yang dipilih tidak ada')
else:
    angka1 = float(input('Angka pertama: '))
    angka2 = float(input('Angka kedua: '))

    if operasi == 1:
        hasil = angka1 + angka2
        op = "+"
    elif operasi == 2:
        hasil = angka1 - angka2
        op = "-"
    elif operasi == 3:
        hasil = angka1 * angka2
        op = "*"
    elif operasi == 4:
        hasil = angka1 / angka2
        op = "/"
    elif operasi == 5:
        hasil = angka1 % angka2
        op = "%"

    print('Hasil dari',angka1,op,angka2,'=',hasil)