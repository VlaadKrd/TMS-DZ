import os
path = input('Введите директорию: ')

def control(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
           print('Спускаемся', path + '/'+i)
           control(path+'/'+i, level+1)
           print('Возвращаемся в', path)
control(path)