from itertools import zip_longest
def transpose(text):
    output = ''
    splitted = text.splitlines()
    for index, row in enumerate(splitted):
        future_max = max(len(r) for r in splitted[index:])
        splitted[index] = row.ljust(future_max, " ")
    for i in zip_longest(*splitted, fillvalue = ""):
        output += "".join(i) + "\n"
    return output[:-1]