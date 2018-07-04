def summation(num):
    i = 0

    while i <= num:
        i = i =+1

        return num + summation(num-1) if num > 1 else 1
