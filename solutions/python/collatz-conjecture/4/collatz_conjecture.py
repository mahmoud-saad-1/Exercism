"""Module to calculate Collatz Conjecture steps."""

def steps(number):
    """Return the number of steps to reach 1 using the Collatz algorithm."""
    # 1. Validation
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    # 2. Base Case (Brakes)
    if number == 1:
        return 0
    
    # 3. Step Calculation (use // for integer division)
    next_number = number * 3 + 1 if number % 2 else number // 2
    
    # 4. Recursive Call to ITSELF
    return 1 + steps(next_number)