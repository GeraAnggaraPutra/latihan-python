print("## Program Python Menghitung Luas belah Ketupat ##")
print("==================================================")
print()

diagonal1 = float(input('Input panjang diagonal 1: '))
diagonal2 = float(input('Input panjang diagonal 2: '))

def luas(d1, d2):
    return round(d1 *d2 * 0.5,2)

print('Luas belah ketupat = ', luas(diagonal1, diagonal2))