def convert(number):
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = ""

    for factor, sound in sounds:
        if number % factor == 0:
            result += sound

    return result if result else str(number)
