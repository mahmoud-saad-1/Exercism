def answer(question):
    if not question.startswith("What is"):
        raise ValueError("unknown operation")
    if question == 'What is?':
        raise ValueError('syntax error')
    clean_sentence = question.replace("?", "").replace("What is ", "").replace("multiplied by", "multiplied").replace("divided by", "divided")
    words = clean_sentence.split()
    if not words:
        raise ValueError('syntax error')
    answer = 0
    current_op = "plus"
    expecting_number = True
    for word in words:
        try:
            number = int(word)
            if not expecting_number:
                raise ValueError('syntax error')
            if current_op == "plus":
                answer += number
            elif current_op == "minus":
                answer -= number
            elif current_op == "multiplied":
                answer *= number
            elif current_op == "divided":
                answer /= number
            expecting_number = False
            
        except ValueError as e:
            # Check if this was our custom syntax error from above
            if str(e) == "syntax error": raise e 
        
            if word in ["plus", "minus", "multiplied", "divided"]:
                if expecting_number: 
                    raise ValueError("syntax error")
                current_op = word
                expecting_number = True 
            else:
                raise ValueError("unknown operation")
            
    if expecting_number:
        raise ValueError("syntax error")
    return int(answer)