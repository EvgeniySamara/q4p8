# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
# файл. JSON файл содержит данные о продуктах (название, цена, количество на
# складе). В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv.
# Подсказка № 1
# Используйте json.load() для чтения данных из JSON файла. Функция json.load()
# позволяет загрузить данные из JSON файла в виде Python объекта, например, списка
# словарей.
# Подсказка № 2
# Используйте csv.DictWriter для записи данных в CSV файл. Функция
# csv.DictWriter позволяет записывать данные в CSV файл, где каждый словарь из
# списка становится одной строкой в CSV.
# Подсказка № 3
# Обеспечьте правильное управление строками в CSV файле. При записи в CSV файл
# используйте параметр newline='' в open(), чтобы избежать дополнительных пустых
# строк между записями на Windows.


import json
import csv
import os

def read_json(file):
    with open (file,'r') as f:
        return json.load(f)

def write_csv(data,file='ex3.csv'):
    with open (file,'w',newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile,fieldnames=['name', 'price', 'quantity'], delimiter=';')
        csvwriter.writeheader()
        for row in data:
            csvwriter.writerow(row)


if __name__=='__main__':
    write_csv(read_json(os.path.join('zad_3','products.json')))
