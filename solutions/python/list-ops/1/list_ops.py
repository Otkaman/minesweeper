def append(list1, list2):
    return list1 + list2


def concat(lists):
    lst = lists
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            result.append(lst[i][j])
    
    return result
    

def filter(function, list=[]):
    lst = list
    for item in lst:
        if not function(item):
            lst.remove(item)
    return lst


def length(list):
    return len(list)


def map(function, list=[]):
    lists = []
    for indx in list:
        lists.append(function(indx))
    return lists

from functools import * 

def foldl(function, list, initial):
    return reduce(function, list, initial)

def foldr(function, list, initial):
    return reduce(function, list[::-1], initial)

def reverse(list):
    return list[::-1]
