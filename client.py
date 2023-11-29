import http.client
import json

# Define the server host and port
host = "localhost"
port = 8080

# Create an HTTP connection to the server
conn = http.client.HTTPConnection(host, port)

# Define the payment authorization request as a dictionary
payment_request = {
    "card_number": "1234-5678-9012-3456",
    "expiration_date": "12/25",
    "cvv": "123",
    "amount": 800
}

# Encode the payment authorization request as JSON
json_payment_request = json.dumps(payment_request)

# Define the path for the POST request
path = "/authorize_payment"

# Set the headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

try:
    # Send a POST request to the server with the JSON payment authorization request
    conn.request("POST", path, json_payment_request, headers)

    # Get the response from the server
    response = conn.getresponse()

    # Read and decode the response data
    response_data = response.read().decode()

    # Print the response data
    print(response_data)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the connection
    conn.close()
