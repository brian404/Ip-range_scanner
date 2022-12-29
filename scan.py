import requests

def scan_range(start_ip, end_ip):
    for i in range(start_ip, end_ip+1):
        try:
            ip = f"http://{i}"
            response = requests.get(ip)
            print(f"{ip}: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"{ip}: ConnectionError")

start_ip = int(input("Enter the starting IP address: "))
end_ip = int(input("Enter the ending IP address: "))

scan_range(start_ip, end_ip)
