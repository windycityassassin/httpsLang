from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a mock endpoint for processing payment authorization
@app.route('/make-payment', methods=['POST'])
def make_payment():
    try:
        print("Received POST request to /make-payment")

        # Parse JSON data from the request
        payment_data = request.get_json()

        card_number = payment_data["card_number"]
        expiration_date = payment_data["expiration_date"]
        cvv = payment_data["cvv"]
        amount = float(payment_data["amount"])

        # Simulate a failure when the payment amount is above a certain limit
        failure_limit = 1000  # Set your failure limit (e.g., $1000)
        if amount > failure_limit:
            error_response = {
                "status": "Error",
                "message": "Payment authorization failed. Payment amount exceeds the limit."
            }
            return jsonify(error_response), 400  # Return JSON error response with HTTP status 400 (Bad Request)

        # Payment authorization logic
        authorization_code = "AUTH12345"  # Simulated authorization code
        response_data = {
            "status": "Success",
            "message": "Payment authorized successfully.",
            "authorization_code": authorization_code
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
    app.run(host='localhost', port=5000)
