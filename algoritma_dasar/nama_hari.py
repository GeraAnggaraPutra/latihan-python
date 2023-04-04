print("## Program Python Menentukan Nama Hari ##")
print("==================================================")

x = int(input('input angka hari (1-7): '))

match x:
    case 1:
      print('Hari ke-',x,'adalah senin')
    case 2:
      print('Hari ke-',x,'adalah selasa')
    case 3:
      print('Hari ke-',x,'adalah rabu')
    case 4:
      print('Hari ke-',x,'adalah kamis')
    case 5:
      print('Hari ke-',x,'adalah jumat')
    case 6:
      print('Hari ke-',x,'adalah sabtu')
    case 7:
      print('Hari ke-',x,'adalah minggu')
    case _:
      print('Pilihan tidak tersedia')