
import paymentgateway
import retryservice
import app_constants as app_const
import validator

cheappayment_constant = app_const.cheappayment_val
expensivepayment_constant1 = app_const.expensivepayment_val1
expensivepayment_constant2 = app_const.expensivepayment_val2
premiumpayment_constant = app_const.premiumpayment_val

cheap_retry = app_const.cheap_payment_retry
premium_retry = app_const.premimum_payment_retry

def process(request):
    print(request)
    
    response = None
    
    #Validate Request

    validatetion_resp = validator.validateFields(request)
    if validatetion_resp['Status'] == 'false':
        return validatetion_resp
    
    # Process Payment
    amount = abs(int(request["Amount"]))
    
    if amount < int(cheappayment_constant):
        response = paymentgateway.CheapPaymentGateway()
        
        return response
    elif int(expensivepayment_constant1) <= amount <= int(expensivepayment_constant2):
        response = paymentgateway.ExpensivePaymentGateway()
        if response == False:
            print("Retry the process")
            response = retryservice.retry_cheappayment(cheap_retry)
            
        return response
    elif amount > premiumpayment_constant:
        response = paymentgateway.PremiumPaymentGateway()
        if response == False:
            print("Retry up to 3 times")
            response = retryservice.retry_premiumpayment(premium_retry)
        
        return response
    else:
        return None
    
    

