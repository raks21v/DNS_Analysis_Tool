from flask import Flask, render_template, request, jsonify
import dns.resolver
import dns.query
import dns.rdatatype
import time
import socket

app = Flask(__name__)

# Function to calculate the security score based on DNS features
def calculate_security_score(dnssec_status, valid_records):
    # Basic score (max 100)
    score = 100

    # Deduct points based on DNSSEC status
    if dnssec_status == "Not Signed":
        score -= 20  # Penalize for lack of DNSSEC

    # Deduct points if records are missing or invalid
    if not valid_records:
        score -= 30  # Penalize for missing or invalid DNS records

    # Score adjustments based on other factors (could be customized further)
    # Here we assume a simple model where faster response time increases score
    return max(0, score)  # Ensure score doesn't go below 0

# Route for the main page (where the DNS tool UI is located)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle DNS analysis for the entered domain
@app.route('/analyze', methods=['POST'])
def analyze():
    domain = request.form.get('domain')
    if domain:
        try:
            # Start the timer to calculate response time
            start_time = time.time()

            # Get the IP address for the domain using socket
            ip_address = socket.gethostbyname(domain)

            # Query DNS for DNSSEC status and other details
            resolver = dns.resolver.Resolver()
            resolver.timeout = 5
            resolver.lifetime = 5

            # Query for DNSSEC status (this checks for DNSSEC records)
            dnssec_status = "Not Signed"
            try:
                dnssec_response = resolver.resolve(domain, 'DNSKEY')
                if dnssec_response:
                    dnssec_status = "Signed"
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                dnssec_status = "No DNSSEC found"

            # Check for valid DNS records (A, CNAME, MX, etc.)
            valid_records = False
            try:
                resolver.resolve(domain, 'A')  # Check for A record
                resolver.resolve(domain, 'MX')  # Check for MX record
                valid_records = True  # If A and MX records are found, it's considered valid
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                valid_records = False

            # Calculate response time
            response_time = round((time.time() - start_time) * 1000, 2)  # in milliseconds

            # Calculate the security score based on DNSSEC status and valid records
            security_score = calculate_security_score(dnssec_status, valid_records)

            # Return the results
            return jsonify({
                'ipAddress': ip_address,
                'responseTime': f'{response_time} ms',
                'dnssecStatus': dnssec_status,
                'securityScore': f'{security_score}/100'
            })

        except Exception as e:
            return jsonify({'error': f"Error: {str(e)}"})
    return jsonify({'error': 'No domain provided'})

if __name__ == '__main__':
    app.run(debug=True)
