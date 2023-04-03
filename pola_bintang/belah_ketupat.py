print("## Program Python Belah Ketupat Bintang ##")
print("====================================")
print()

lebar_belahketupat = int(input('Input lebar belah ketupat: '))
print()

for i in range(lebar_belahketupat):
    print(' ' * (lebar_belahketupat-i),end='')
    print('* ' * (i+1))
for i in range(1,lebar_belahketupat):
    print(' ' * (i+1),end='')
    print('* ' * (lebar_belahketupat-i))

print()

for i in range(lebar_belahketupat):
    for j in range(lebar_belahketupat-i):
        print(' ', end='')
    for k in range(i+1):
        print('* ',end='')
    print()
for i in range(1,lebar_belahketupat):
    for j in range(i+1):
        print(' ', end='')
    for k in range(lebar_belahketupat-i):
        print('* ',end='')
    print()