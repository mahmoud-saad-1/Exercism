BANDS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCE = {'grey' : '0.05%', 'violet' : '0.1%', 'blue' : '0.25%', 'green' : '0.5%', 'brown' : '1%', 'red' : '2%', 'gold' : '5%', 'silver' : '10%'}

def resistor_label(colors):
    # Fix 1: Handle the 1-band edge case explicitly
    if len(colors) == 1:
        if colors[0] == "black":
            return "0 ohms"
        return f"{BANDS.index(colors[0])} ohms"

    # Separate digits, multiplier, and tolerance dynamically
    if len(colors) == 4:
        digit_bands = colors[:2]
        multiplier = colors[2]
    else:  # 5 bands
        digit_bands = colors[:3]
        multiplier = colors[3]
        
    # Extract tolerance band (always the last element)
    tolerance_band = colors[-1]

    # Calculate raw ohms
    code = "".join(str(BANDS.index(c)) for c in digit_bands)
    ohms = int(code) * (10 ** BANDS.index(multiplier))

    # Fix 2 & 3: Use >= boundaries and standard division (/) instead of floor division (//)
    if ohms >= 1_000_000_000:
        scaled_ohms = ohms / 1_000_000_000
        unit = "gigaohms"
    elif ohms >= 1_000_000:
        scaled_ohms = ohms / 1_000_000
        unit = "megaohms"
    elif ohms >= 1_000:
        scaled_ohms = ohms / 1_000
        unit = "kiloohms"
    else:
        scaled_ohms = ohms
        unit = "ohms"

    
    return f"{scaled_ohms:g} {unit} ±{TOLERANCE[tolerance_band]}"