def steps(number):
    k=0
    if number > 0:
        while True:
            if number%2==0:
                number //= 2
                k+=1
            else:
                if number==1:
                    return k
                else:
                    number = number * 3 + 1
                    k+=1
    else:  
        raise ValueError("Only positive integers are allowed")      