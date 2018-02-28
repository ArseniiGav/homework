import os
import chardet

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def create_sql_file_list():
    migrations_dir = os.path.join(current_dir, migrations)
    file_list = os.listdir(path = migrations_dir)
    sql_file_list = list()
    for file in file_list:
        if file.endswith('.sql'):
            sql_file_list.append(file)
    return sql_file_list
        
def read_files(name):
    with open(os.path.join(current_dir, migrations, name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data.lower()
    return data

def search_by_lines(sql_file_list):
    file_list = sql_file_list
    while True:
        str_input = input("Введите строку, (если хотите остановить введите: да): ", )
        str_input = str_input.lower()
        tapering_list = list()
        if str_input == "да":
            print('Stoped')
            break
        for name in file_list:
            if str_input in read_files(name):
                tapering_list.append(name)
                print(name)
        print("Количество файлов: {}".format(len(tapering_list)))
        file_list = tapering_list
        
if __name__ == '__main__':
    search_by_lines(create_sql_file_list())
    pass