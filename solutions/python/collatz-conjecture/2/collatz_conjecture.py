def steps(number):
    count = 0
    if number > 0:
        while True:
            if number%2==0:
                number //= 2
                count += 1
            else:
                if number==1:
                    return count
                else:
                    number = number * 3 + 1
                    count += 1
    else:  
        raise ValueError("Only positive integers are allowed")      