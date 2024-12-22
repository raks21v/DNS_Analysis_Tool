# DNS_Analysis_Tool
This project is a Flask-based web application designed to analyze the DNS records of a given domain and assess its security features, such as DNSSEC status and valid DNS records. The application provides an IP address lookup, response time measurement, DNSSEC verification, and a security score for the domain based on certain factors.

Features

DNSSEC Verification: Checks whether the domain has DNSSEC (DNS Security Extensions) enabled or not. The presence of DNSSEC enhances the security of DNS lookups, preventing certain types of attacks such as DNS spoofing.

DNS Records Validation: The application checks for the existence of key DNS records, such as A (Address) and MX (Mail Exchange) records, which are essential for ensuring that a domain is properly configured.

Response Time Measurement: Measures the time it takes to resolve the domain’s DNS queries, helping assess the speed and performance of DNS resolution.

Security Scoring: The application calculates a security score based on DNSSEC status and the validity of DNS records, providing an overall security assessment. The score ranges from 0 to 100, with deductions for missing DNSSEC records or invalid DNS entries.

How It Works

The user inputs a domain in the web interface.
The backend Flask app performs several DNS queries to gather information, including:
Resolving the domain's IP address.
Checking for the domain's DNSSEC status.
Verifying the presence of A and MX records.
The application calculates the response time and generates a security score based on the DNS configuration.
The results are displayed on the frontend, including the domain's IP address, response time, DNSSEC status, and the overall security score.
Technologies Used
Flask: A micro web framework used for building the web application.
dns.resolver: A library used to query DNS records and check DNSSEC status.
socket: Used to resolve the domain to its corresponding IP address.
JavaScript: To handle dynamic interactions on the frontend (if applicable).
#How to Run
Clone this repository to your local machine:
git clone https://github.com/yourusername/dns-security-analyzer.git
cd dns-security-analyzer

Install the required dependencies:
pip install -r requirements.txt

Run the Flask application:
python app.py
Open your browser and go to http://localhost:5000/ to use the tool.

#Example Output
The results returned by the analysis include:

IP Address: The resolved IP address of the domain.
Response Time: The time it took to resolve the DNS queries (in milliseconds).
DNSSEC Status: Whether the domain is signed with DNSSEC or not.
Security Score: A numerical score (out of 100) indicating the security of the domain based on its DNS configuration.
Contribution
Feel free to contribute to this project! Open a pull request for bug fixes, improvements, or new features.
