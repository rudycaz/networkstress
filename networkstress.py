import requests
import threading

# Function to send requests
def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

# Define the URL for your local server
target_url = "http://localhost:8080"  # replace with your test server <-----------------------

# Number of threads (simulating multiple clients)
num_threads = 5

# Create and start threads to send requests
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request, args=(target_url,))
    threads.append(thread)
    thread.start()

# Join threads to keep them running
for thread in threads:
    thread.join()
