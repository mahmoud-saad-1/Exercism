BANDS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def value(colors):
    code = ''
    for color in colors[:2]:
        code += f"{BANDS.index(color)}"
    return int(code)
    