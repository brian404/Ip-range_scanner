import requests
import ipaddress

def check_http_status(ip_address):
  try:
    r = requests.get("http://" + str(ip_address))
    if r.status_code == 200:
      return "Success"
    else:
      return "Error"
  except:
    return "Error"

def scan_cidr(cidr):
  subnet = ipaddress.ip_network(cidr)
  for ip in subnet:
    status = check_http_status(ip)
    print(str(ip) + ": " + status)

# Scan the CIDR range 1.2.3.4/24
scan_cidr("1.2.3.4/24")
