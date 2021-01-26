import paymentgateway
import time


def retry_cheappayment(max_tries):
    for i in range(max_tries):
        try:
            time.sleep(0.5)
            return paymentgateway.CheapPaymentGateway()
        except Exception:
            continue
        
def retry_premiumpayment(max_tries):
    for i in range(max_tries):
        try:
            time.sleep(0.5)
            return paymentgateway.PremiumPaymentGateway()
        except Exception:
            continue