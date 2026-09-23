def is_isogram(string):
    chars = []
    for char in string.lower():
        if char != ' ' and char != '-':
            if char in chars:
                return False
            chars.append(char)
    return True
