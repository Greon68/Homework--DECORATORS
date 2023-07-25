# УСЛОВИЕ:
# Доработать декоратор logger в коде ниже.
# Должен получиться декоратор, который записывает
# в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Функция test_1 в коде ниже также должна отработать без ошибок.

# import os
#
#
# def logger(old_function):
#     ...
#
#     def new_function(*args, **kwargs):
#         ...
#
#     return new_function
#
#
# def test_1():
#
#     path = 'main.log'
#     if os.path.exists(path):
#         os.remove(path)
#
#     @logger
#     def hello_world():
#         return 'Hello World'
#
#     @logger
#     def summator(a, b=0):
#         return a + b
#
#     @logger
#     def div(a, b):
#         return a / b
#
#     assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#     result = summator(2, 2)
#     assert isinstance(result, int), 'Должно вернуться целое число'
#     assert result == 4, '2 + 2 = 4'
#     result = div(6, 2)
#     assert result == 3, '6 / 2 = 3'
#
#     assert os.path.exists(path), 'файл main.log должен существовать'
#
#     summator(4.3, b=2.2)
#     summator(a=0, b=0)
#
#     with open(path) as log_file:
#         log_file_content = log_file.read()
#
#     assert 'summator' in log_file_content, 'должно записаться имя функции'
#     for item in (4.3, 2.2, 6.5):
#         assert str(item) in log_file_content, f'{item} должен быть записан в файл'
#
#
# if __name__ == '__main__':
#     test_1()

import os
import  datetime

path = 'data_file'
if os.path.exists(path):
    os.remove(path)

def logger(old_function):

    def new_function(*args, **kwargs):
        # Список аргументы+результат
        item_list = []
        # print(f'Текущие дата и время - {datetime.datetime.now()}')
        date = datetime.date.today()
        print(f'Дата вызова функции - {date}')
        time = datetime.datetime.now().time()
        print(f'Время вызова функции -{time} ')
        name = old_function.__name__
        print(f'Имя функции- {name}')
        argums = f'{args=},{kwargs=}'
        print (argums)

        result = old_function(*args, **kwargs)
        print(f'Результат вызова функции - {result}')

        # Записываем в выходные данные значения кортежа args:
        for el in args:
            item_list.append(el)

        # Записываем в выходные данные значения словаря kwargs:
        for key,val in kwargs.items():
            item_list.append(val)

        item_list.append(result)
        # Преобразуем список в кортеж
        item = tuple(item_list)
        print(f'Кортеж данных - {item}')
        print()

        # Запись в файл main.log
        with open('main.log', 'a') as file:
            file.write(str(date))
            file.write('\n')
            file.write(str(time))
            file.write('\n')
            file.write(str(name))
            file.write('\n')
            file.write(argums)
            file.write('\n')
            file.write(str(result))
            file.write('\n')
            file.write(str(item))
            file.write("\n\n")

        return result

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'


    @logger
    def summator(a, b=0):
        return a + b


    @logger
    def div(a, b):
        return a / b



    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()