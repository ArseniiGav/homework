import subprocess
import shutil
import os

def resize_files():
    process = "convert "
    size =  " -resize 200 "
    if os.path.exists("Result") == False:
        os.mkdir("Result")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = os.listdir(path = current_dir)
    for file in file_list:
        out_name = "out_" + file
        subprocess.run(process + file  + size + out_name)

def move_files(): 
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_list = os.listdir(path = current_dir)
    for file in file_list:
        if file.startswith('out_'):
            shutil.move(file, 'Result')

resize_files()
move_files()
