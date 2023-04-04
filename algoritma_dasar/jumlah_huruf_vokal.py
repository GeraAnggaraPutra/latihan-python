print("## Program Python Menghitung Jumlah Huruf Vokal ##")
print("==================================================")

x = input('Input kata/kalimat: ')

vokal = 0
for i in x:
    if (i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o'):
        vokal = vokal + 1

if vokal > 0:
    print('Jumlah huruf vokal = ', vokal)
else:
    print('Huruf vokal tidak ditemukan')