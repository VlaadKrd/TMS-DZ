num1 = int(input('Введи число №1 '))
num2 = int(input('Введи число №2 '))
num3 = num1 * num2

print(num3)

if num3 % 2 == 0:
    print('Число четное')
    exit(0)
else:
    print('Число нечетное')
    exit(1)