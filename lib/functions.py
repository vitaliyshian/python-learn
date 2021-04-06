'''
Модуль
'''
def unique(raw, sort = False):
    '''
    Получает уникальние значения из масива
    :param raw: List
    :param sort: Boolean
    :return: List
    '''
    has_letter = False
    has_numeral = False

    for val in raw:
        if isinstance(val, str):
            has_letter = True
        if isinstance(val, int):
            has_numeral = True

    if has_letter and has_numeral:
        print("Пожалуйста передайте массив с однородными данными")
        return []

    un = []
    for val in raw:
        if val not in un:
            un.append(val)
    un.sort(reverse=sort)
    return un

def is_poly(word = ''):
    '''
    Проверяет является ли слово полиндромом  пример-(Мадам) -
    :param word: str
    :return: boolean
    '''
    if not isinstance(word, str):
        print("Не правильный формат данных!")
        return False

    lower_word = word.lower()
    if lower_word == lower_word[::-1]:
        return True
    else:
        return False

def print_type(val):
    '''
    Выводит тип данных
    :param val: any
    :return: None
    '''
    if isinstance(val, str):
        print("Тип данных Строка %s" % val)
    elif isinstance(val, int):
        print("Тип данных числовой %s" % val)
    elif isinstance(val, float):
        print("Тип данных вещественый %s" % val)
    elif isinstance(val, list):
        print("Тип данных массив %s" % val)
    else:
        print("Неизвестный тип Данных!!!")

def min(arr):
    '''
    Возвращеет минимальное число из масива
    :param arr: list
    :return: int | float | None
    '''
    if not isinstance(arr, list):
        print("Не массив!!!")
        return None
    if len(arr) == 0:
        print("Массив не имеет елементов!!!")
        return None
    m = arr[0]
    for val in arr:
        if val < m:
            m = val
    return m

def max(arr):
    '''
    Возвращает максимальное число из масива
    :param arr: list
    :return: int | float | None
    '''
    if not isinstance(arr, list):
        print("Не массив")
        return None
    if len(arr) == 0:
        print("Массив не имеет елементов!!!")
        return None
    b = 0
    for val in arr:
        if val > b:
            b = val
    return b

def search(arr, user_input):
    '''
    Ищет совпаденя в масиве
    :param arr: list
    :param user_input: str
    :return: str | None
    '''
    for val in arr:
        if user_input.lower() == val.lower():
            return val
    return None