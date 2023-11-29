from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# Define a mock endpoint for the payment authorization form
@app.route('/')
def payment_form():
    return render_template('form.html')


# Define a mock endpoint for processing payment authorization
@app.route('/authorize_payment', methods=['POST'])
def authorize_payment():
    try:
        print("Received POST request to /authorize_payment")

        # Parse form data
        card_number = request.form.get("card_number")
        expiration_date = request.form.get("expiration_date")
        cvv = request.form.get("cvv")
        amount = float(request.form.get("amount"))

        print("Card Number:", card_number)
        print("Expiration Date:", expiration_date)
        print("CVV:", cvv)
        print("Amount:", amount)

        # Simulate credit card authorization based on a credit limit criterion
        credit_limit = 1000  # Define a credit limit (adjust as needed)

        if amount <= credit_limit:
            authorization_code = "AUTH12345"  # Simulated authorization code
            response_data = {
                "status": "Success",
                "message": "Payment authorized successfully.",
                "authorization_code": authorization_code
            }
        else:
            response_data = {
                "status": "Failure",
                "message": "Payment authorization failed. Exceeded credit limit."
            }

        return jsonify(response_data), 200  # Return JSON response with HTTP status 200 (OK)

    except Exception as e:
        error_response = {
            "status": "Error",
            "message": str(e)
        }
        print("Error:", e)
        return jsonify(error_response), 400  # Return JSON error response with HTTP status 400 (Bad Request)


if __name__ == '__main__':
    # Run the server with regular HTTP (not HTTPS) on port 8080
    app.run(host='localhost', port=8080)
