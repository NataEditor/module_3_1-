calls = 0
spisok_lis = ['Яблоко', 'двадцать', 'СолнЦе', 1, 10, 100, True]


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(stroka):
    count_calls()
    a = len(stroka)
    b = stroka.upper()
    c = stroka.lower()
    info_tuple = a, b, c
    return info_tuple


def is_contains(a=str(), b=[]):
    count_calls()
    if a.lower() in (str(item).lower() for item in b):
        return True
    else:
        return False


print('"это первое задание подсчет колличества вызовов функции"')
print(count_calls(), count_calls(), count_calls())

print('"это второе задание информация о введенной строке"')
print('Введите вашу строку ')  # string
string = str(input())
print(string_info(string))

print('"это третье задание "')
print('Введите вашу строку ')  # string
string2 = str(input())
print(is_contains(string2, spisok_lis))
print(count_calls())
