BANDS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def label(colors):
    code = ''
    for color in colors[:2]:
        code += f"{BANDS.index(color)}"
    ohms = int(code) * 10 ** BANDS.index(colors[2])
    if ohms > 1000000000:
        return f"{ohms // 1000000000} gigaohms"
    elif ohms > 1000000:
        return f"{ohms // 1000000} megaohms"
    elif ohms > 1000:
        return f"{ohms // 1000} kiloohms"
    else:
        return f"{ohms} ohms"
