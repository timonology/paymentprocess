import logger as log

def PremiumPaymentGateway():
    try:
        print("Premium Payment Gateway")
        message = "Premium Payment Gateway"
        resp = { 'Status': 'true', 'Message': "Premium Payment Gateway Successful" }
        return resp
    except Exception as e:
        log.push('exception on PremiumPaymentGateway: ' +str(e))
        return { 'Status': 'false', 'Message': "Unable to  Process Premium Payment" }
    

def ExpensivePaymentGateway():
    try:
        print("Expensive Payment Gateway")
        message = "Expensive Payment Gateway"
        resp = { 'Status': 'true', 'Message': "Expensive Payment Gateway Successful" }
        return resp
    except Exception as e:
        log.push('exception on ExpensivePaymentGateway: ' +str(e))
        return { 'Status': 'false', 'Message': "Unable to  Process Expensive Payment" }
    
    

def CheapPaymentGateway():
    try:
        print("Cheap Payment Gateway")
        message = "Cheap Payment Gateway"
        resp = { 'Status': 'true', 'Message': "Cheap Payment Gateway Successful" }
        return resp
    except Exception as e:
        log.push('exception on CheapPaymentGateway: ' +str(e))
        return { 'Status': 'false', 'Message': "Unable to  Cheap Premium Payment" }