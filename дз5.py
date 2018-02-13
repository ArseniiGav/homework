group_of_students = {
        "1": {"Имя": "Иван", "Фамилия": "Горбатов", "Пол": "Мужской", \
              "Опыт": "Да", "Дз": [6, 10, 9, 9, 5], "Экзамен": 10},
        "2": {"Имя": "Аня", "Фамилия": "Захарова", "Пол": "Женский", \
              "Опыт": "Нет", "Дз": [7, 9, 5, 7, 8], "Экзамен": 8},      
        "3": {"Имя": "Аня", "Фамилия": "Карушева", "Пол": "Женский", \
              "Опыт": "Да", "Дз": [7, 8, 9, 9, 7], "Экзамен": 8}, 
        "4": {"Имя": "Вика", "Фамилия": "Свиридова", "Пол": "Женский", \
              "Опыт": "Да", "Дз": [7, 9, 7, 9, 1], "Экзамен": 10},
        "5": {"Имя": "Егор", "Фамилия": "Грин", "Пол": "Мужской", \
              "Опыт": "Нет", "Дз": [8, 8, 8, 9, 6], "Экзамен": 10},
        "6": {"Имя": "Василий", "Фамилия": "Иванов", "Пол": "Мужской", \
              "Опыт": "Нет", "Дз": [5, 9, 5, 7, 9], "Экзамен": 8},  
        "7": {"Имя": "Сергей", "Фамилия": "Иванов", "Пол": "Мужской", \
              "Опыт": "Нет", "Дз": [6, 8, 9, 8, 7], "Экзамен": 8},
        }
         
def average_score(*args):
    home_work_sum = 0
    exam_sum = 0
    number_of_students = []
    for value in group_of_students.values():
        if tuple(value["Пол"]) == args:
            number_of_students.append(value)
            for score in value["Дз"]:
                home_work_sum += score
            exam_sum += value["Экзамен"]
        elif tuple(value["Опыт"]) == args:
            number_of_students.append(value)
            for score in value["Дз"]:
                home_work_sum += score
            exam_sum += value["Экзамен"]
        elif args == tuple():
            number_of_students.append(value)
            for score in value["Дз"]:
                home_work_sum += score
            exam_sum += value["Экзамен"]    
    average_score_home_work = home_work_sum / (len(number_of_students) * len(value["Дз"]))  
    exam_average_score = exam_sum / len(number_of_students)
    return round(average_score_home_work, 2), round(exam_average_score, 2)
           

def best_student():
    student_params_list = []
    integral_score_j_list = []
    for student_number, student_params in group_of_students.items():
        sum_home_work_score = 0
        for j in student_number:
            if student_number == j:
                for i in student_params["Дз"]:
                    sum_home_work_score += i
                integral_score_j = 0.6 * sum_home_work_score / 5 + \
                0.4 * student_params["Экзамен"]
                integral_score_j_list.append(integral_score_j)
            student_params_list.append(student_params["Имя"]) 
    max_score_list = []
    max_score = 0
    name_student_list = []
    position_best_student_in_list = []
    for i in integral_score_j_list:
         if i > max_score:
            max_score = i
    for i, score in enumerate(integral_score_j_list):
         if max_score == score:
            max_score_list.append(max_score)
            position_best_student_in_list.append(i)
    return name_student_list, max_score, len(max_score_list), student_params_list, position_best_student_in_list

def run():
    print("Справка: Команда 1 - выводит средние оценки по группе в целом.\
 Команда 2 - выводит средние оценки мужчин и женщин и\
 студeтов с опытом и без.\
 Команда 3 - выводит лучшего/лучших студенов по группе.\
 Команда 4 - выводит все средние оценки сразу.")
    while True:
        comand = int(input("Введите команду: "))
        if comand == 1:
            print('Средняя оценка за дз по группе: {} \
                   \nСредняя оценка за экзамен по группе: {}' \
                   .format(average_score()[0], average_score()[1]))
        elif comand == 2:
            print('\n\nСредняя оценка за дз по группе у мужчин: {} \
                  \nСредняя оценка за экзамен по группе у мужчин: {}\
                  \nСредняя оценка за дз по группе у женщин: {}\
                  \nCредняя оценка за экзамен по группе у женщин: {} \
                  \n\nСредняя оценка за дз у студентов с опытом: {} \
                  \nСредняя оценка за экзамен у студентов с опытом: {}, \
                  \nСредняя оценка за дз у студентов без опыта: {} \
                  \nСредняя оценка за экзамен у студентов без опыта: {}'\
                  .format(average_score(*"Мужской")[0], average_score(*"Мужской")[1], \
                  average_score(*"Женский")[0], average_score(*"Женский")[1], average_score(*"Да")[0], \
                  average_score(*"Да")[1], average_score(*"Нет")[0], average_score(*"Нет")[1]))
        elif comand == 3:
            if len(best_student()[4]) == 1:
                print('Лучший cтудент: {} с интегральной оценкой: {}'\
                      .format(best_student()[3][best_student()[4][0]], best_student()[1]))
            elif len(best_student()[3]) == best_student()[2]:
                print('Все студенты имеют одну и ту же интегральную оценку: ', best_student()[1])
            else:
                i = 0
                name_best_student_list = []
                while i <= (best_student()[2] - 1):
                    name_best_student_list.append(best_student()[3][best_student()[4][i]])
                    i += 1
                name_best_student_str = ", ".join(name_best_student_list)
                print('Лучшие cтуденты: {} с интегральной оценкой: {}'\
                      .format(name_best_student_str, best_student()[1]))
        elif comand == 4:
            print('\nСредняя оценка за дз по группе: {} \
            \nСредняя оценка за экзамен по группе: {} \
            \n\nСредняя оценка за дз по группе у мужчин: {}\
            \nСредняя оценка за экзамен по группе у мужчин: {}\
            \nСредняя оценка за дз по группе у женщин: {}\
            Средняя оценка за экзамен по группе у женщин: {} \
            \n\nСредняя оценка за дз у студентов с опытом: {} \
            \nСредняя оценка за экзамен у студентов с опытом: {}, \
            \nСредняя оценка за дз у студентов без опыта: {} \
            \nСредняя оценка за экзамен у студентов без опыта: {} \
            '.format(average_score()[0], average_score()[1], average_score(*"Мужской")[0], \
            average_score(*"Мужской")[1], average_score(*"Женский")[0], average_score(*"Женский")[1], average_score(*"Да")[0], \
            average_score(*"Да")[1], average_score(*"Да")[0], average_score(*"Да")[1]))
        else:
            print("Неправильно введена команда!")


run()



