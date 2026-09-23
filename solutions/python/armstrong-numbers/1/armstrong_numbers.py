def is_armstrong_number(number):
    length = len(str(number))
    sum = 0
    for n in range(length):
        sum += int(str(number)[n]) ** length
    return sum == number
