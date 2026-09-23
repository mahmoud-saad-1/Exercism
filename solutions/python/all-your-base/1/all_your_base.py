def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for d in digits:
        if not (0 <= d < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    total = 0 
    output = []
    for n in digits:
        total = total * input_base + n
    if total == 0:
        output = [0]
    while total != 0:
        output += [total % output_base]
        total = total // output_base
    output.reverse()
    return output
