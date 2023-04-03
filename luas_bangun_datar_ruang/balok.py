print("## Program Python Menghitung Luas Permukaan Balok ##")
print("==================================================")
print()

panjang = float(input('Input panjang: '))
lebar = float(input('Input lebar: '))
tinggi = float(input('Input tinggi: '))

def luas(p, l, t):
    return round(2 * ((p*l) + (p*t) + (l*t)),2)

print('Luas permukaan balok = ', luas(panjang, lebar, tinggi))