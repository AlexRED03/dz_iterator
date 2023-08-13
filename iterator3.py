


def f(list0):
    list1 = []
    for i in list0:
        if type(i) != list:
            list1.append(i)
        else:
            list1 += f(i)
    return list1


list_of_lists_2 = [[['a'], ['b', 'c']],['d', 'e', [['f'], 'h'], False],[1, 2, None, [[[[['!']]]]], []]]


print(f(list_of_lists_2))