import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# Replace <ip_address> with the actual IP address
URL = "http://<ip_address>/api/generate"
PAYLOAD = {
    "model": "phi3",
    "prompt": "How can I substitute a wrong article from Amazon?",
    "stream": False
}
HEADERS = {'Content-Type': 'application/json'}
N = 100  # Number of requests to send

def send_request():
    response = requests.post(URL, headers=HEADERS, data=json.dumps(PAYLOAD))
    return response.status_code, response.text

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request) for _ in range(N)]
        for future in as_completed(futures):
            status_code, text = future.result()
            print(f"Status Code: {status_code}, Response: {text}")

if __name__ == "__main__":
    main()