def proverb(*args, qualifier=None):
    if not args:
        # Guardrail for empty inputs remains intact
        return []
        
    result = []
    
    # 1. Process all paired lines cleanly with ZERO if/else blocks!
    for current_item, next_item in zip(args, args[1:]):
        result.append(f"For want of a {current_item} the {next_item} was lost.")
        
    # 2. Handle the final line cleanly outside the loop
    first_item = f"{qualifier} {args[0]}" if qualifier else args[0]
    result.append(f"And all for the want of a {first_item}.")
        
    return result