# Задача 2. Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.
# Подсказка № 1
# Используйте функцию glob.glob() для поиска всех JSON файлов в указанной
# директории.
# Подсказка № 2
# Откройте каждый JSON файл с помощью json.load() и добавьте данные в общий
# список. Функция json.load() позволяет прочитать содержимое JSON файла и
# преобразовать его в Python объект. Используйте list.extend() для объединения
# данных.
# Подсказка № 3
# Сохраните объединенные данные в новый JSON файл с помощью json.dump(). После
# объединения данных, используйте json.dump() для записи списка в новый JSON
# файл.

import csv
import glob
import os
import json



def find_files(path):
    filelist = [f.split('\\')[1] for f in glob.glob('zad_2/*')]
    return filelist

def read_json(file):
    with open(file,'r') as f:
        jdata = json.load(f)
        return jdata




if __name__=='__main__':
    target_dir = r'C:\Users\User\PycharmProjects\Gbpractic\q4p8'
    if os.path.isdir(target_dir):
        filelist = find_files(target_dir)
        for file in filelist:
            print(read_json(os.path.join('zad_2',file)))

    else:
        print('Некорректный каталог')

