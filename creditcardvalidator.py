import logger as log

def ValidateCard(card):
    try:
        print("validating card")
        card_number = list(card.strip())
        
        check_digits = card_number.pop()
        card_number.reverse()
        
        processed_digits = []
        
        for index, digits in enumerate(card_number):
            if index % 2 == 0:
                doubled_digits = int(digits) * 2
                
                if doubled_digits > 9:
                    doubled_digits = doubled_digits - 9
                    
                processed_digits.append(doubled_digits)
            else:
                processed_digits.append(int(digits))
                
        total = int(check_digits) + sum(processed_digits)
        
        if total % 10 == 0:
            print("Card Is Valid")
            return True
        else:
            print("Card is Invalid")
            return False
    except Exception as e:
        log.push('exception on ValidateCard: ' +str(e))
        return None