import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Serve the payment form at the root URL
@app.route('/', methods=['GET'])
def show_payment_form():
    return render_template('payment.html')

# Handle the payment submission
@app.route('/make-payment', methods=['POST'])
def make_payment():
    try:
        payment_data = {
            "card_number": request.form["card_number"],
            "expiration_date": request.form["expiration_date"],
            "cvv": request.form["cvv"],
            "amount": request.form["amount"]
        }

        # Send the payment data as a JSON request to the processing server
        processing_server_url = 'http://localhost:5000/make-payment'
        response = requests.post(processing_server_url, json=payment_data)

        return response.text, response.status_code
    except Exception as e:
        error_response = {
            "status": "Error",
            "message": str(e)
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(host='localhost', port=8081)