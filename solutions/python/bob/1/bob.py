def response(hey_bob):
    stripped = hey_bob.strip()

    if len(stripped) > 0 and hey_bob.isupper() and stripped[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif len(stripped) > 0 and stripped[-1] == '?':
        return "Sure."
    elif hey_bob.isspace() or len(hey_bob) == 0:
        return "Fine. Be that way!"
    else:
        return "Whatever."