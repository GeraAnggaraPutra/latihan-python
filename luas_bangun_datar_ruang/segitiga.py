print("## Program Python Menghitung Luas Segitiga ##")
print("====================================")
print()

alas = float(input('Input alas segitiga: '))
tinggi = float(input('Input tinggi segitiga: '))

def luas(a, t):
    return round(alas * tinggi * 0.5,2)

print('Luas segitiga = ', luas(alas, tinggi))