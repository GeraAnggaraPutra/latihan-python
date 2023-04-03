print("## Program Python Konversi Desimal ke Biner ##")
print("==================================================")

n = int(input('Input angka desimal: '))

print(bin(n).replace("0b","")) # cara cepatt

a = []
i = 0
while n > 0:
    a.append(n % 2)
    n = n // 2
    i = i + 1
    
print('Angka binernya adalah: ', end='')

for i in range(i-1, -1, -1):
    print(a[i],end='')
