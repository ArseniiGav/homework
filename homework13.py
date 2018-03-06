import subprocess
import shutil
import os

source = "Source"
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, source)
os.chdir(source)

def resize_files():
    process = "convert "
    size =  " -resize 200 "
    if not os.path.exists("Result"):
        os.mkdir("Result")
    file_list = os.listdir(path = source_dir)
    for file in file_list:
        out_name = "out_" + file
        subprocess.run(process + file + size + out_name)

def move_files(): 
    file_list = os.listdir(path = source_dir)
    for file in file_list:
        if file.startswith('out_'):
            shutil.move(file, 'Result')

if __name__ == '__main__':
    resize_files()
    move_files()
    pass
