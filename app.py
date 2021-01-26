from flask import Flask, request
from flask_restplus import Resource, Api, fields
from process_model import PaymentModel as pmodel
import paymentprocessservice as processservice

app = Flask(__name__)
api = Api(app, version= '1.0', title= 'Python Coding Test', description= 'Coding Test')

paymentmodel = pmodel(api)



@api.route('/paymentprocess/api/SendEmail', methods=['POST'])
class ProcessPaymentClass(Resource):
    @api.expect(paymentmodel)
    def post(self, **kwargs):
        data = request.json
        response = processservice.process(data)
        if response['Status'] == 'true':
            return response, 200
        elif response['Status'] == 'false':
            return response, 400
        else:
            return { 'Status': 'false', 'Message': 'An Unexpected Error occured. Please try again later' }, 500



if __name__ == '__main__':
    app.run(debug=True)