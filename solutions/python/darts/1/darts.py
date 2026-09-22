import math

def score(x, y):
    d = math.sqrt(x**2 + y**2)
    if d <= 1:
        return 10
    elif d <= 5:
        return 5
    elif d <= 10:
        return 1
    else:
        return 0
