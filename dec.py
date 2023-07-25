

import  datetime


def logger(path):
    ''' Параметрический декоратор . Параметр
    path - папка , куда записываютися
    результаты работы декоратора'''

    def __logger(old_function):

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
            item = tuple(item_list)
            print(f'Кортеж данных - {item}')

            # Запись в файл paths
            with open(path, 'a') as file:
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
                print()
            return result

        return new_function

    return __logger
