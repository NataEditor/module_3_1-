calls = 0
spisok_lis = ['Яблоко', 'двадцать', 'СолнЦе', 1, 10, 100, True]
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(str):
    a = len(str)
    b = str.upper()
    c = str.lower()
    info_tuple = a, b, c
    return print(info_tuple)

def is_contains(a=str(),b = []):
    if a.lower() in (item.lower() for item in a):
        print('false')
    else: print('true')
   



print('"это первое задание подсчет колличества вызовов функции"')
print(count_calls(), count_calls(), count_calls())

print('"это второе задание информация о введенной строке"')
print('Введите вашу строку ') # string
string = str(input())
string_info(string)

print('"это третье задание "')
print('Введите вашу строку ') # string
str = str(input())
is_contains(str, spisok_lis)