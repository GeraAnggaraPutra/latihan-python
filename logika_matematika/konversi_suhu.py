print("## Program Python Menghitung Suhu ##")
print("==================================================")

suhu = float(input('Input suhu celsius: '))

fahrenheit = (9/5 * suhu )+ 32
kelvin = suhu + 273.15
reamur = (4/5) * suhu

print(suhu,'derajat Celcius = ', fahrenheit,'derajat Fahrenheit')
print(suhu,'derajat Celcius = ', kelvin,'derajat Kelvin')
print(suhu,'derajat Celcius = ', reamur,'derajat Reamur')