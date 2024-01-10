import random
import time
from collections import namedtuple


ExerciseParams = namedtuple(
    'ExerciseParams',
    ['question', 'operation', 'max_value'])


exercises = {
    1: ExerciseParams('{} + {} = ', lambda x, y: x + y, 1000),
    2: ExerciseParams('{} - {} = ', lambda x, y: x - y, 1000),
    3: ExerciseParams('{} * {} = ', lambda x, y: x * y, 20),
}


def training():
    name = input('привет, как тебя зовут?\n')
    a = int(input(f'''Привет, {name}, я Анна. 
Давай порешаем примеры.
Задай количество примеров которое ты хочешь решить.
'''))
    print(f'''Правила просты: ты решаешь {a} примеров а я говорю верно или нет.
В конце я вывожу количество ошибок и время.
''')
    errors = 0
    s = time.time()
    for _ in range(a):
        k = random.randint(1, 3)
        r1, r2 = random.randint(1, exercises[k].max_value), random.randint(1, exercises[k].max_value)
        if r1 < r2:
            r1, r2 = r2, r1
        n = int(input(exercises[k].question.format(r1, r2)))
        if exercises[k].operation(r1, r2) == n:
            print('Верно')
        else:
            print('Неверно')
            errors += 1
    f = time.time()
    print(f'Ты решил {a} примеров за {round(f-s, 1)} секунд. Допустил {errors} ошибок.')


if __name__ == '__main__':
    training()
