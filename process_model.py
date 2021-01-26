from flask_restplus import fields

def PaymentModel(api):
    model = api.model('PaymentModel', {
        'CreditCardNumber': fields.String(required=True),
        'CardHolder': fields.String(required=True),
        'ExpirationDate': fields.DateTime(required=True),
        'SecurityCode': fields.String(),
        'Amount': fields.String()
    })
    return model