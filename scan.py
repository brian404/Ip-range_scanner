import ipaddress
import requests

# Prompt the user to enter a CIDR range
cidr_range = input("Enter a CIDR range to scan: ")

# Convert the CIDR range to a network object
network = ipaddress.ip_network(cidr_range)

# Iterate over all of the addresses in the network
for address in network:
   # Send a request to the address and get the response
   try:
       response = requests.get(f"http://{address}", timeout=1)
       status = response.status_code
       status_text = "Alive"
   except:
       status = None
       status_text = "Dead"

   if status:
       print(f"{address}: {status_text} (HTTP {status})")
   else:
       print(f"{address}: {status_text}")

