# Задание 1. Работа с основными данными
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
# pickle. Для дочерних объектов указывайте родительскую директорию. Для
# каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов.
# Подсказка № 1
# Для рекурсивного обхода используйте функцию os.walk(). Эта функция генерирует
# имена файлов и директорий в указанной директории и ее поддиректориях. Внутри
# цикла можно разделять файлы и директории и собирать информацию о них.
# Подсказка № 2
# Используйте os.path.getsize() для определения размера файла. Эта функция
# возвращает размер файла в байтах. Для директорий вы можете использовать
# рекурсивный обход для вычисления общего размера всех вложенных файлов.
# Подсказка № 3
# Для сбора информации о каждом объекте создайте словарь. Словарь должен
# содержать такие ключи, как 'name', 'path', 'type', 'size', и 'parent'.
# Используйте os.path.basename() для получения имени родительской директории.
# Подсказка № 4
# Сохраняйте данные в разные форматы с помощью соответствующих библиотек.
# Используйте json.dump() для JSON, csv.DictWriter() для CSV и
# pickle.dump() для Pickle.

import os
import json
import csv
import pickle



def get_size(path):
    """  Возвращает размер файла или директории.
    """
    if os.path.isfile(path): # Если путь - файл, возвращаем его размер
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0

# Если путь - директория, рекурсивно вычисляем размер всех файлов в директории
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def traverse_directory(directory):
    """Рекурсивно обходит директорию и возвращает информацию о файлах
    и директориях."""
    result = []
    # Обход директории с помощью os.walk, который возвращает корневую директорию, поддиректории и файлы
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)
            # Добавление информации о текущем объекте в список результата
            result.append({
            'name': name,
            'path': path,
            'type': 'directory' if is_dir else 'file',
            'size': size,
            'parent': parent
            })
    return result

def save_to_json(data, file = 'testjson.json'):
    with open (file,"w") as f:
        json.dump(data,f)


def save_to_csv(data, file = 'testcsv.csv'):
    with open (file,"w") as f:
        writer = csv.DictWriter(f,fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, file = 'test.pickle'):

    with open(file, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)



# def obhod(target_dir):
#     res = dict()
#     for root,dirs,files in os.walk(target_dir):
#         for file in files:
#             # print(os.path.join(root,file))
#
#
#             # os.path.isfile(os.path.join(root, file))
#             res[file] = ([root,file,os.path.getsize(os.path.join(root, file))])
#         for file in files:
#             # print(os.path.join(root,file))
#
#
#             # os.path.isfile(os.path.join(root, file))
#             res[file] = ([root,dir,os.path.getsize(os.path.join(root, file))])
#
#     return res


if __name__ == '__main__':
    target_dir = r'c:\Users\User\PycharmProjects\Gbpractic\q4p8'

    if not os.path.isdir(target_dir):
        print('Директория не найдена')
    else:
        # res = obhod(target_dir)
        # print(os.path.basename(f"{target_dir}\\ex1.py"))
        res = traverse_directory(target_dir)
        print (*res, sep='\n')
        save_to_json(res)
        save_to_csv(res)
        save_to_pickle(res)