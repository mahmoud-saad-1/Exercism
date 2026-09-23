def is_paired(input_string):
    var = []
    
    # Mapping closers to their openers makes the code cleaner
    pairs = {')': '(', ']': '[', '}': '{'}

    for letter in input_string:
        # 1. If it's an opener, add to memory
        if letter in "([{":
            var.append(letter)
        
        # 2. If it's a closer, validate the top of the stack
        elif letter in ")]}":
            # If we see a closer but memory is empty -> False
            if not var:
                return False
            
            # If the closer doesn't match the last opener -> False
            if var.pop() != pairs[letter]:
                return False

    # 3. Final check: If anything is left in var, it's unbalanced
    return len(var) == 0
