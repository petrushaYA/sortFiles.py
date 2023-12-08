import os
import hashlib
import csv
import time



# def check_duplicate_files(folder_path):
#     file_paths = {}
#     file_duplicates = {}
#
#     for foldername, _, filenames in os.walk(folder_path):
#         for filename in filenames:
#             file_path = os.path.join(foldername, filename)
#             if filename in file_paths:
#                 with open('files_with_the_same_name.csv', 'a', newline='') as csvfile:
#                     writer = csv.writer(csvfile, delimiter=';')
#                     writer.writerow([filename, file_paths[filename], file_path])
#                 print(f"Дубликаты файла {filename} найдены в:")
#                 print(f"1. {file_paths[filename]}")
#                 print(f"2. {file_path}")
#                 file_duplicates[filename] = file_path
#             else:
#                 file_paths[filename] = file_path
#     csvfile.close()

def check_duplicate_hashes1212(folder_path):
    file_hashes = {}
    file_paths = {}

    for foldername, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = hashlib.md5(file_content).hexdigest()

                if filename in file_hashes and file_hash == file_hashes[filename]:
                    with open('files_with_same_name_same_content.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';')
                        writer.writerow([filename, file_paths[filename], file_path])

                    print(f"Файлы {filename} имеют одинаковые названия и содержимые содержимое:")
                    print(f"1. {file_paths[filename]}, хеш: {file_hashes[filename]}")
                    print(f"2. {file_path}, хеш: {file_hash}\n")
                else:
                    file_hashes[filename] = file_hash
                    file_paths[filename] = file_path


def check_duplicate_hashes(folder_path):
    file_hashes = {}
    file_paths = {}

    for foldername, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = hashlib.md5(file_content).hexdigest()

                if filename in file_hashes and file_hash != file_hashes[filename]:
                    with open('files_with_same_name_but_diff_content.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';')
                        writer.writerow([filename, file_paths[filename], file_path])

                    print(f"Файлы {filename} имеют разное содержимое:")
                    print(f"1. {file_paths[filename]}, хеш: {file_hashes[filename]}")
                    print(f"2. {file_path}, хеш: {file_hash}\n")
                else:
                    file_hashes[filename] = file_hash
                    file_paths[filename] = file_path

def check_thesame_files(folder_path):
    all_hashes = {}

    for foldername, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)

            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = hashlib.md5(file_content).hexdigest()

                if file_hash in all_hashes:
                    with open('files_with_the_dif_name_but_same_content.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';')
                        name1 = os.path.basename(all_hashes[file_hash])  # Присваиваем значения здесь
                        name2 = os.path.basename(file_path)
                        if name1 != name2:
                            writer.writerow([name1, all_hashes[file_hash], name2, file_path])  # Используем здесь
                    print(f"Файлы с одинаковым хешем найдены:")
                    print(f"1. {name1}  {all_hashes[file_hash]}")
                    print(f"2. {name2}  {file_path}\n")
                else:
                    all_hashes[file_hash] = file_path



file = open('path.txt', "r", encoding='utf-8')
path = file.read()

check_duplicate_hashes1212(path)
print('\n')
check_duplicate_hashes(path)
print('\n')
check_thesame_files(path)  # r'C:\Users\temych\PycharmProjects\sortFiles\from'
print('\n')
print("Завершено!")
time.sleep(3)
file.close()

