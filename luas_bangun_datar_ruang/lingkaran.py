print("## Program Python Menghitung Luas Lingkaran ##")
print("====================================")
print()

jari_jari = float(input('Input jari - jari lingkaran: '))

def luas(r):
    return round(r * r * 3.14,2)

print('Luas lingkaran = ', luas(jari_jari))