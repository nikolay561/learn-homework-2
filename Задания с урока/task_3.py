# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

students_repeat = {}

for student_name in students:
    if student_name['first_name'] not in students_repeat:
        students_repeat[student_name['first_name']] = 1
    else:
        students_repeat[student_name['first_name']] += 1

for students in students_repeat:
    print(f'{students}: {students_repeat[students]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

student_names = {}

for names in students:
    if names['first_name'] not in student_names:
        student_names[names['first_name']] = 1
    else:
        student_names[names['first_name']] += 1

quantity = 0
most_popular_name = None
for name in student_names:
    if student_names[name] > quantity:
        most_popular_name = name
        quantity = student_names[name]
print(f'Самое частое имя среди учеников: {most_popular_name}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

def most_popular_name(school_students):
    number_repetitions_names = {}

    for key in school_students:
        if key['first_name'] not in number_repetitions_names:
            number_repetitions_names[key['first_name']] = 1
        else:
            number_repetitions_names[key['first_name']] += 1

    quantity = 0
    most_popular_name = None

    for name in number_repetitions_names:
        if number_repetitions_names[name] > quantity:
            quantity = number_repetitions_names[name]
            most_popular_name  = name

    return most_popular_name

print(f'Самое частое имя в классе 1: {most_popular_name(school_students[0])}.\n'
    f'Самое частое имя в классе 2: {most_popular_name(school_students[1])}.')
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

male_2a = 0
female_2a = 0

for name in school[0]['students']:
    if name['first_name'] in is_male:
        if is_male[name['first_name']] == True:
            male_2a += 1
        elif is_male[name['first_name']] == False:
            female_2a += 1

male_3c = 0
female_3c = 0

for name in school[1]['students']:
    if name['first_name'] in is_male:
        if is_male[name['first_name']] == True:
            male_3c += 1
        elif is_male[name['first_name']] == False:
            female_3c += 1

print(f'В классе 2а {female_2a} девочки и {male_2a} мальчика.\n'
    f'В классе 3c {female_3c} девочки и {male_3c} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a