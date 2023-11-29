from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to track payments for each card
card_payments = {}

# Define a maximum total spend for each card (adjust as needed)
max_total_spend = {
    "1234-5678-9012-3456": 2000,
    "5678-1234-3456-9012": 1500,
    # Add more card numbers and limits as needed
}

# Simulated external credit card processing system
def settle_payment(card_number, amount):
    # Simulate a settlement request with an external system
    # In a real-world scenario, you would use a payment gateway API
    return True  # Return True for success, or False for failure

# Define an endpoint to settle payments
@app.route('/settle-payment', methods=['POST'])
def settle_payment_request():
    try:
        # Parse the settlement request data from the JSON payload
        settlement_data = request.get_json()

        # Extract credit card information
        card_number = settlement_data.get("card_number")
        amount = settlement_data.get("amount")

        # Check if the card number exists in the tracking dictionary
        if card_number not in card_payments:
            return jsonify({"status": "Failure", "message": "Card not found"}), 400

        # Check if the settlement request is valid
        if amount <= 0:
            return jsonify({"status": "Failure", "message": "Invalid settlement request"}), 400

        # Check if the card has enough balance for settlement
        if card_payments[card_number] < amount:
            return jsonify({"status": "Failure", "message": "Insufficient balance for settlement"}), 400

        # Perform the settlement with the external processing system
        if settle_payment(card_number, amount):
            card_payments[card_number] -= amount
            return jsonify({"status": "Success", "message": "Settlement successful"}), 200
        else:
            return jsonify({"status": "Failure", "message": "Settlement failed with external system"}), 500

    except Exception as e:
        error_response = {
            "status": "Error",
            "message": str(e)
        }
        return jsonify(error_response), 400  # Return JSON error response with HTTP status 400 (Bad Request)

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
