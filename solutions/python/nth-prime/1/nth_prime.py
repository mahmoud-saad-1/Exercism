def prime_generator():
    candidate = 2
    while True:
        # Check if the candidate is prime
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False  # Found a divisor! Not prime.
                break             # Stop checking this candidate
        
        # If it survived the loop without is_prime becoming False, it's prime!
        if is_prime:
            yield candidate
            
        candidate += 1  # Move to the next number for the next turn

def prime(number):
    if number <= 0:
        raise ValueError('there is no zeroth prime')
        
    # 1. Spin up the infinite generator pipeline
    g = prime_generator()
    
    # 2. Pull from the pipeline exactly 'number' times
    for _ in range(number):
        current_prime = next(g)
        
    # 3. Return the final one we grabbed
    return current_prime