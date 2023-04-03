print("## Program Python Menghitung Luas Persegi Panjang ##")
print("====================================")
print()

panjang_persegi_panjang = float(input('Input panjang persegi panjang: '))
lebar_persegi_panjang = float(input('Input lebar persegi panjang: '))
luas = panjang_persegi_panjang * lebar_persegi_panjang
print('Luas persegi panjang= ', round(luas,2))

def luas(panjang_persegi_panjang, lebar_persegi_panjang):
    return round(panjang_persegi_panjang * lebar_persegi_panjang,2)

print('Luas persegi panjang= ', luas(panjang_persegi_panjang, lebar_persegi_panjang))