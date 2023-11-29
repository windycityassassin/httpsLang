from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

# Define the URL of the processing server
processing_server_url = "http://localhost:8080/authorize_payment"  # Replace with the actual URL of your processing server

# Define a mock endpoint for the payment form
@app.route('/payment')
def payment_form():
    return render_template('payment.html')

# Define an endpoint for processing payments
@app.route('/make-payment', methods=['POST'])
def make_payment():
    try:
        # Parse the payment data from the form submission
        card_number = request.form.get("card_number")
        expiration_date = request.form.get("expiration_date")
        cvv = request.form.get("cvv")
        amount = float(request.form.get("amount"))

        # Prepare the payment request as a dictionary
        payment_request = {
            "card_number": card_number,
            "expiration_date": expiration_date,
            "cvv": cvv,
            "amount": amount
        }

        # Convert the payment request to JSON
        json_payment_request = json.dumps(payment_request)

        # Send the payment request to the processing server
        response = requests.post(processing_server_url, data=json_payment_request, headers={'Content-Type': 'application/json'})

        # Check the response from the processing server
        if response.status_code == 200:
            response_data = response.json()
            return jsonify(response_data), 200
        else:
            return jsonify({"status": "Failure", "message": "Payment processing server error"}), 500

    except Exception as e:
        error_response = {
            "status": "Error",
            "message": str(e)
        }
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(host='localhost', port=5000)  # Run the UI server on port 5000
