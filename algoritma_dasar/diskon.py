print("## Program Python Diskon Potongan Harga ##")
print("==================================================")

harga = int(input('Total belanja: '))

if(harga >= 100000 and harga <= 500000):
    total = harga - (0.1 * harga)
    print('Selamat, anda mendapatkan diskon 10%')
elif(harga > 500000 and harga <= 1000000):
    total = harga - (0.2 * harga)
    print('Selamat, anda mendapatkan diskon 20%')
elif(harga > 1000000):
    total = harga - (0.3 * harga)
    print('Selamat, anda mendapatkan diskon 30%')
else:
    total = harga

print('Total bayar: Rp.',total)