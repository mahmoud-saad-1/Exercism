class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # 1. Clean spaces and immediately enforce the length guard
        num = self.card_num.replace(' ', '')
        if len(num) <= 1:
            return False
            
        # 2. Character guard clause (exits early if invalid characters exist)
        if not num.isdigit():
            return False
            
        # 3. Main logic runs flat, no deep nesting!
        digits = [int(n) for n in num][::-1]
        
        for index, n in enumerate(digits):
            if index % 2 == 1:
                doubled = n * 2
                # If doubled is greater than 9, subtract 9, otherwise keep it
                digits[index] = doubled - 9 if doubled > 9 else doubled
                    
        return sum(digits) % 10 == 0