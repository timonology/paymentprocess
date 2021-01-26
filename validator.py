import validationservice


def validateFields(request):
    try:
        print("validate fields")
        
        fields_checker = validationservice.field_isrequired(request)
        if fields_checker['Status'] == 'false':
            return fields_checker
        
        expirydate_resp = validationservice.date_checker(request['ExpirationDate'])
        if expirydate_resp['Status'] == 'false':
            return expirydate_resp
        
        creditcard_resp = validationservice.creditcard_checker(request["CreditCardNumber"])
        if creditcard_resp['Status'] == 'false':
            return creditcard_resp
        
        securitycode_resp = validationservice.securitycode_checker(request['SecurityCode'])
        if securitycode_resp['Status'] == 'false':
            return securitycode_resp
        
        return {'Status': 'true', 'Message': 'Validation Successful'}
    except Exception as e:
        print(e)