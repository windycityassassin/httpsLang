from server import app
import ssl

if __name__ == '__main__':
    # Specify the paths to your SSL certificate and private key files
    ssl_certfile = '/Users/apv/PycharmProjects/dcwe4/server-cert.crt'
    ssl_keyfile = '/Users/apv/PycharmProjects/dcwe4/server-key.pem'

    # Create an SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(ssl_certfile, ssl_keyfile)

    # Run the Flask app with SSL/TLS enabled on port 8080 (HTTPS)
    app.run(host='0.0.0.0', port=8080, ssl_context=ssl_context)
