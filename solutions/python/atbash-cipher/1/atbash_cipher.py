def encode(plain_text):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    filtered_plain_text = "".join([char for char in plain_text.lower() if char.isalnum()])
    translated = filtered_plain_text.translate(table)
    chunks = []
    for i in range(0, len(translated), 5):
        chunks.append(translated[i:i+5])
    final_output = " ".join(chunks)
    return final_output


def decode(ciphered_text):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')
    plain = ciphered_text.replace(" ", "") 
    return plain.translate(table)
