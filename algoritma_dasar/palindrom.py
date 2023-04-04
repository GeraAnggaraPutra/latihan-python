print("## Program Python Cek Kata Palidrom ##")
print("==================================================")
# menurut wikipedia
# palindrom adalah sebuah kata, bilangan, frasa, atau susunan karakter lain yang serupa jika
# dibaca dengan urutan terbalik ataupun tidak, seperti katak atau apa

x = input('Input kata/kalimat: ')
palindrom = True

panjang_x = len(x)

for i in range(panjang_x//2):
    if (x[i] != x[panjang_x-i-1]):
        palindrom = False
        break

if palindrom:
    print(x, 'adalah palindrom!')
else:
    print(x, 'bukan palindrom!')