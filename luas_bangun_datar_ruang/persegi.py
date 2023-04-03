print("## Program Python Menghitung Luas Persegi ##")
print("====================================")
print()

sisi_persegi = float(input('Input panjang sisi persegi: '))
luas = sisi_persegi * sisi_persegi
print('Luas persegi = ', round(luas,2))

def luas(sisi_persegi):
    return round(sisi_persegi * sisi_persegi,2)

print('Luas persegi = ', luas(sisi_persegi))