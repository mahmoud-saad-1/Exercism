import string

def rows(letter):
    letters = string.ascii_uppercase[:ord(letter) - ord('A') + 1]
    n = len(letters) - 1 
    result = []

    # build top half
    for i, ch in enumerate(letters):
        leading = n - i
        if i == 0:
            row = " " * leading + ch + " " * leading
        else:
            inner = 2 * i - 1
            row = " " * leading + ch + " " * inner + ch + " " * leading
        result.append(row)

    # mirror bottom half
    result += list(reversed(result[:-1]))

    return result
