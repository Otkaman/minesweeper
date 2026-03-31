def del1(n, k):
    count = []
    if k>0:
        for i in range(k, n, k):
            count.append(i)
        return count
    return [0]
    

def sum_of_multiples(limit, multiples):
    arr = []
    for i in range(len(multiples)):
        arr = arr + del1(limit,multiples[i])
    arr.sort()
    result = sum(list(set(arr)))
    return result  
