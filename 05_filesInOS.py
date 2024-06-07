# -*- coding: utf-8 -*-

import os
import time

my_path = 'C:/UrbanUniversity/01_strings_and_bytes'
directory = os.path.normpath(my_path) # нормализованная директория
cnt = 0
print('-'*70)
Header_txt = 'Файлы в директории:'
print(f'{Header_txt:-^70}')
print(f'{directory:-^70}')
for dir1, dirs, files in os.walk(directory): # По родительской директории
    for file in files: # По найденным файлам
        cnt += 1
        file_path = os.path.join(dir1, file) # "Правильный" путь к файлу "file"
        file_time_sec = os.path.getmtime(file_path) # Время в секундах
        file_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time_sec))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print('-'*70)
        print(f'{cnt:>4}. Файл:{' '*2}   |{file}')
        print(f'Время изменения:|{file_time}')
        print(f'Размер:{' '*7}  |{file_size}')
        print(f'Родитель:{' '*7}|{parent_dir}')
TheEnd = ' The End '
print(f'{TheEnd:-^70}')