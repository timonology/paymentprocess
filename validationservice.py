import creditcardvalidator
from datetime import datetime



def creditcard_checker(card_number):
    response = creditcardvalidator.ValidateCard(card_number)
    print(response)
    
    if response == True:
        return { 'Status': 'true', 'Message': "Credit Card Valid" }
    else:
        return { 'Status': 'false', 'Message': "Credit Card Number Invalid" }
    
    return response

def date_checker(expirationdate):
    currentdate = datetime.now()
    print(expirationdate)
    print(currentdate)
    
    if expirationdate >= str(currentdate):
        return { 'Status': 'true', 'Message': "Expiration date is OK" }
    else:
        return { 'Status': 'false', 'Message': "You cannot proceed because your Card has already expired" }

def securitycode_checker(securitycode):
    if len(securitycode) == 3:
        return { 'Status': 'true', 'Message': "Security Code Valid" }
    else:
        return { 'Status': 'false', 'Message': "Security Code cannot be greater than 3 digits" }
    
def field_isrequired(request):
    expdate = request['ExpirationDate']
    creditcard = request['CreditCardNumber']
    securitycode = request['SecurityCode']
    cardholder = request['CardHolder']
    amount = request['Amount']
    if expdate == "":
        return { 'Status': 'true', 'Message': f"ExpirationDateis required" }
    elif creditcard == "":
        return { 'Status': 'false', 'Message': f"CreditCardNumber is required" }
    elif securitycode == "":
        return { 'Status': 'false', 'Message': f"SecurityCode is required" }
    elif cardholder == "":
        return { 'Status': 'false', 'Message': f"CardHolder is required" }
    elif amount == "":
        return { 'Status': 'false', 'Message': f"Amount is required" }
    else:
        return { 'Status': 'true', 'Message': f"OK" }