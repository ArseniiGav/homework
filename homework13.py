import subprocess
import shutil
import os

def resize_files(current_dir, source):
    source_dir = os.path.join(current_dir, source)
    os.chdir(source_dir)
    process = os.path.join(current_dir, "convert.exe ")
    size =  " -resize 200 "
    file_list = os.listdir(path = source_dir)
    for file in file_list:
        subprocess.run(process + os.path.abspath(file) + size +\
                       os.path.join(current_dir, "out_" + file))

def move_files(current_dir, result):
    os.chdir(current_dir)
    if not os.path.exists("Result"):
        os.mkdir("Result")
    result_dir = os.path.join(current_dir, result)
    result_file_list = os.listdir(path = result_dir)
    file_list = os.listdir(path = current_dir)
    for file in file_list:
        if file.startswith('out_'):
            if result_file_list == []:
                shutil.move(file, 'Result')

if __name__ == '__main__':
    resize_files(os.path.dirname(os.path.abspath(__file__)), "Source")
    move_files(os.path.dirname(os.path.abspath(__file__)), "Result")
    pass

