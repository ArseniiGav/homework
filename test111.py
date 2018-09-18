import random
randomr = input('Если Вы хотите заполнить матрицы случайными числа от -10 до 10 введите "yes", если нет, то введите "no" и заполните самостоятельно  ', )


def create_matrix(M,N):
    if randomr.lower() == 'yes':
        matrix = [[random.randrange(-10,10) for y in range(M)] for x in range(N)]
    elif randomr.lower() == 'no':
        matrix = []
        for i in range(N):
            string = input('Введите элементы без запятых и пробелов (количество элементов {}) строки {} '.format(M,i+1))
            list_string = list(string)
            float_string = []
            for ele in list_string:
                ele_f = float(ele)
                float_string.append(ele_f)
            matrix.append(float_string)
    return matrix        


def input_data():
    M = int(input('Введите количество столбцов матрицы ', ))
    N = int(input('Введите количество строк матрицы ', ))
    matrix = create_matrix(M,N)
    return matrix


print('Cоздадим первую матрицу')
matrix1 = input_data()
print('Cоздадим вторую матрицу')
matrix2 = input_data()


def multiplication_matrix(matrix1, matrix2):
    sum = 0
    result_string = []
    result_matrix = []
    if len(matrix2)!=len(matrix1[0]):
        print("Матрицы не могут быть перемножены")        
    else:
        count_strings1 = len(matrix1)
        count_columns1 = len(matrix1[0])
        count_columns2 = len(matrix2[0])
        for z in range(0,count_strings1):
            for j in range(0,count_columns2):
                for i in range(0,count_columns1):
                   sum += matrix1[z][i] * matrix2[i][j]
                result_string.append(sum)
                sum = 0
            result_matrix.append(result_string)
            result_string=[]           
    return result_matrix

result_matrix = multiplication_matrix(matrix1, matrix2)
print(matrix1)
print(matrix2)
print(result_matrix)