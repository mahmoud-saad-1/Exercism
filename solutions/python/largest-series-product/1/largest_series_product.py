import math

def largest_product(series, size):
    # 1. Validation Block
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if size == 0:
        return 1
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    # 2. Convert string to integers
    series_int = [int(i) for i in series]

    # 3. Slide through and compute maximum product
    totals = []
    for n in range(len(series_int) - size + 1):
        slice_digits = series_int[n : n + size]
        totals.append(math.prod(slice_digits))  # Multiplies all numbers in the slice instantly

    return max(totals)