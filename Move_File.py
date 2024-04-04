import os
import shutil

from_dir = "C:/Users/91967/Downloads"
to_dir = "C:/Users/91967/OneDrive/Desktop/Documents_File"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == '':
        continue

    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Documents_File"
        path3 = to_dir + '/' + "Documents_File" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)