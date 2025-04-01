"""задачи яндекса с интервью"""

def get_min_distance(string_text):
    '''
Дана некая строка, в которой есть буквы X, Y, O. Которые идут произвольно
Требуется написать функцию которая возвращает минимальное растояние между X и Y

примеры: 
    OOOOXOOOOXYO - 1
    XOOOOOOYOOX - 3
    XYOOOOOXOYO - 1
'''
    x = 'X'
    y = 'Y'
    x_index = None
    y_index = None
    min_distance = 0
    for index, letter in enumerate(string_text):
        if letter == x:
            x_index = index
        elif letter == y:
            y_index = index
        if x_index is not None and y_index is not None:
            current_distance = 0
            current_distance = y_index - x_index if y_index > x_index else x_index - y_index
            if min_distance == 0 or min_distance > current_distance:
                min_distance = current_distance
    return min_distance




def diff_list(left_list, rigth_list):
    """Для двух массивов целых чисел длины N, для всех К от 1 до N
    посчитать количество общих чисел на префиксах длины N

    [1, 1, 2, 3]
    [2, 1, 3, 1]
    [0, 1, 2 ]
    """
    result_list = []

    for index in range(len(left_list)):
        result_list.append(len(set(left_list[0:index + 1]) & set(rigth_list[0:index + 1])))

    return result_list

left_list = [1, 1, 2, 3]
rigth_list = [2, 1, 0, 0]

print(get_min_distance('OOOXXOY'))

print(diff_list(left_list, rigth_list))