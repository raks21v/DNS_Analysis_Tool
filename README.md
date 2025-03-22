# 🌐 DNS Analysis Tool

This project is a **Flask-based web application** designed to analyze DNS records of a given domain and assess its security features, such as **DNSSEC status** and valid DNS records. It provides IP address lookup, response time measurement, DNSSEC verification, and a security score.

---

## 🚀 Features
- **DNSSEC Verification:** Checks if the domain has DNSSEC (DNS Security Extensions) enabled, preventing DNS spoofing.
- **DNS Records Validation:** Verifies essential DNS records like A (Address) and MX (Mail Exchange).
- **Response Time Measurement:** Measures the time taken to resolve DNS queries.
- **Security Scoring:** Calculates a security score (0 to 100) based on DNSSEC status and DNS record validity.

---

## ⚙️ How It Works
1. User inputs a domain in the web interface.
2. Backend Flask app performs DNS queries to:
   - Resolve the domain's IP address.
   - Check DNSSEC status.
   - Verify A and MX records.
3. Response time is measured, and a security score is generated.
4. Results are displayed, including IP address, response time, DNSSEC status, and security score.

---

## 🛠️ Technologies Used
- **Flask:** Web framework for the application.
- **dns.resolver:** Queries DNS records and checks DNSSEC.
- **socket:** Resolves domain to its IP address.
- **JavaScript:** Handles frontend dynamic interactions.

---

## 💻 How to Run
```bash
# Clone the repository
git clone https://github.com/yourusername/dns-security-analyzer.git
cd dns-security-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py

# Open your browser
Visit http://localhost:5000/
```

---

## 📊 Example Output
- **IP Address:** Resolved IP address of the domain.
- **Response Time:** Time taken to resolve DNS queries (in ms).
- **DNSSEC Status:** Indicates if the domain is signed with DNSSEC.
- **Security Score:** A score out of 100 based on DNS configuration.

---

## 🤝 Contribution
Contributions are welcome! Feel free to open a pull request for improvements, bug fixes, or new features.

---

🌐 *Secure your domains with confidence!*

