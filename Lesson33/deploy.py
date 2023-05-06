import os

local = 'builds'
#========================== DEV ===========================
dev = 1
rmdev = "~/builds"
adrdev = 'ubuntu@34.212.83.197'
#============================ PROD ========================
prod = 2
rmprod = '~/'
adrprod = ''
#===========================================================
dp = int(input(f'Введите 1 для DEV \nВведите 2 для PROD  '))

if dp == dev:
    print('Вы выбрали DEV окружение')
    print("Копирование имиджа")
    os.system(f'rsync --archive --verbose --progress {local} {adrdev}:{rmdev}')
    print('Копирвание закончено')

elif dp == prod:
    print("Вы выбрали PROD окружение")
    print("Копирование имиджа")
    os.system(f'rsync --archive --verbose --progress ${local} ${userprod}@${ipprod}:${rmprod}')
    print('Копирвание закончено')
else:
    print('Неверный ввод :(')
    exit(1)