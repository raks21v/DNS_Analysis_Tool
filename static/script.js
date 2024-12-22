function analyzeDNS() {
    const domain = document.getElementById("domain").value;

    if (domain.trim() === "") {
        alert("Please enter a domain.");
        return;
    }

    // Send the domain name to the Flask backend
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ domain: domain })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            // Update the result fields with the fetched data
            document.getElementById("domainName").textContent = domain;
            document.getElementById("ipAddress").textContent = data.ipAddress;
            document.getElementById("responseTime").textContent = data.responseTime;
            document.getElementById("dnssecStatus").textContent = data.dnssecStatus;
            document.getElementById("securityScore").textContent = data.securityScore;
        }
    })
    .catch(error => {
        alert("There was an error with the DNS analysis.");
        console.error("Error:", error);
    });
}
