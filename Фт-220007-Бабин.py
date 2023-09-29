mn=0
mx=0
moda=0
modb=0
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < 0:
    moda = -a
else:
    moda = a
if b < 0:
    modb = -b
else:
    modb = b
if moda > modb:
    mn = modb
    mx = moda
else:
    mn = moda
    mx= modb
print("Сумма введенных чисел: ", a + b)
print("Разность введенных чисел: " , a - b , "и" , b - a)
print("Произведение введенных чисел: " , a * b,)
print("Среднее арифметисеские введенных чисел: " , (a + b)/ 2)
print("Разность максимального и минимального по модулю из введенных чисел: " , mx - mn)
print("Частное введенных чисел: ", round(a / b , 2))