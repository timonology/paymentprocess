# paymentprocess

To Run the Flask app. Kindly run the  command below

python app.py

ACTION: POST
http://127.0.0.1:5000/paymentprocess/api/process

SAMPLE PAYLOAD

{
  "CreditCardNumber": "50610XXXXXXXXXX791",
  "CardHolder": "timothy babalola",
  "ExpirationDate": "2021-01-26T16:15:38.000Z",
  "SecurityCode": "191",
  "Amount": "21"
}
