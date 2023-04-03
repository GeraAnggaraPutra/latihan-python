print("## Program Python Menghitung Luas Trapesium ##")
print("==================================================")
print()

sisi_atas = float(input('Input sisi sejajar atas: '))
sisi_bawah = float(input('Input sisi sejajar bawah: '))
tinggi = float(input('Input tinggi: '))

def luas(sa, sb, t):
    return round((sa + sb) * t * 0.5,2)

print('Luas trapesium = ', luas(sisi_atas, sisi_bawah, tinggi))