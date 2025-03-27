"""Mini python programs for practice and better understanding"""
import math

def get_area():
    """01 task Program which accepts the radius of a circle from the user and compute the area"""
    try:
        radius = float(input("Введите радиус круга: "))
        return math.pi * radius**2
    except TypeError:
        print("Допускаются только цифры!")

def check_num():
    """02 task Program to check if a number is positive, negative or zero"""
    try:
        num = float(input("Введите число:  "))
        if num > 0:
            print("positive!")
        elif num < 0:
            print("negative=(")
        else:
            print("zero")
    except ValueError:
        print("Требуется вводить только число!!!")

def check_whether():
    """03 task Program to check whether a number is completely divisible by another number"""
    num1, num2 = input("Введите числа, разделённые пробелами: ").split()
    total = int(num1) // int(num2)
    if total == 0:
        print("неделится!")
    else:
        print("делится!")

def nplus():
    """04 task Program that accepts an integer (n) and computes the value of (n+nn+nnn)"""
    try:
        num = int(input("Введите число:" ))
        print(num + num**2 + num**3)
    except ValueError:
        print("Требуется вводить только число!!!")

def get_volume_sphere():
    """06 task Program to get the volume of a sphere V=4 / 3 πr3"""
    try:
        radius = float(input("Введите число:  "))
        volume = 4 / 3 * math.pi * radius**3
        print("{:.3f}".format(volume)) #три знака после запятой
    except ValueError:
        print("Требуется вводить только число!!!")
        return
    
    print("Текст после экзепта")

def get_between_num_17():
    """07 task Program to get the difference between a given number and 17, difference cannot be negative"""
    num = float(input("Введите число не больше 17:  "))
    try:
        if num > 17:
            print(f"Разница {17 - num:.2f}")
        else:
            print("Число больше 17!")
    except ValueError:
        print("Требуется вводить число!")

def is_string(func):
    '''08 task Program to get a new string from a given string where "Is" has been added to the front'''
    city = 'London'
    string_new = "the Capital of Great Britain"
    string_is = 'is'
    result_string = city + ' ' + string_is + ' ' + string_new
    match func:
        case 'p':
            print(result_string)
        case 'r':
            return(result_string)
        case _:
            print("Неверное значение!")

def string_display_ntimes():
    '''09 task Program to display string n times'''
    for x in range(5):
        print(is_string('r'))

def number_odd():
    """10 task program to find whether a given number is even or odd"""
    try:
        number = int(input("Введите целое число: "))
        if number % 2 == 0:
            print("Число четное!")
        else:
            print("Нечетное!")
    except:
        print("Требуется ввести число!")

def letter_vowel():
    '''11 task Program to test whether a passed letter is a vowel or not'''
    vowel_cyrilic_letters = 'аеёиоуыэюя'
    digits = '1234567890'
    letter = ''
    
    while len(letter) != 1:
        letter = input("Введите одну букву(кирилаца): ")
        if len(letter) > 1:
            print("Одну букву!")

    if letter in vowel_cyrilic_letters:
        print("Гласная!")
    elif letter in digits:
        print("Ненадо вводить цифры о_О")
    else:
        print("Негласная?")      

def get_letter_count():
    '''Дополнительная задача с герератором словаря'''
    #Представим, что хотим сформировать словарь где указать букву-какое кол-во оно встречается в строке. 
    text_string = 'БОльшая строка для расчета ООО'
    text_string = text_string.lower()
    vowel_cyrilic = 'аеёиоуыэюя'
    leter_count_dict = {letter: text_string.count(letter) for letter in set(text_string)
                        if letter in vowel_cyrilic}
    print(leter_count_dict)

def python_book():
    """задачи из книги"""

    #создайте англо русский словарь, с 3 словами
    e2f_dict = dict(dog = 'chien', cat = 'chat', walrus = 'morse')
    print(e2f_dict['walrus'])
    f2e_dict = {f_word: e_word for e_word, f_word in e2f_dict.items()}
    print(f2e_dict['chien'])
    print(set(e2f_dict))

    life_dict = {'animals' : dict(cats = ['Henri', 'Grumpy', 'Lucy'], octopi = {}, emus = {}), 'plants' : {}, 'othe' : {}}
    print(list(life_dict.keys()))
    print(list(life_dict['animals']['cats']))
    squares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
    odd= set(num for num in range(10) if num % 2 != 0)
    print(squares_dict)
    print(odd)

    
class OopsException(Exception):
    print('Caught an oops')

def python_book_1():
    """Задачи связанные с декораторами и исключениями"""
    
    def test(func):
        def wrapper(*args, **kwargs):
            print('Start')
            print(func(*args, **kwargs))
            print('End')
        
        return wrapper
    
    @test
    def get_odds():
        list = [x for x in range(10) if x % 2 != 0]
        count = 0
        for x in list:
            if count == 2:
                return x
            count += 1
        return
    
    def get_exception():
        list = []
        if len(list) < 3:
            raise OopsException
    
    try:
        get_exception()
    
    except OopsException as exc:
        print("Отрабатывает сама ошибка и этот текст")

def recursion():
    def flatten(lol):
        for item in lol:
            if isinstance(item, list):
                for subitem in flatten(item):
                    yield subitem
            else:
                yield item
    lol = [1, 2, [3, 4, 5], [6,[7, 8, 9], [] ]]
    return list(flatten(lol))



print(recursion())