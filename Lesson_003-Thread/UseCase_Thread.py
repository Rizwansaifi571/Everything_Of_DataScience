# Practical Example of threading usecase

'''
import threading
import time
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.google.com', 
    'https://www.tensorflow.org/', 
    'https://www.tensorflow.org/install', 
    'https://www.tensorflow.org/tutorials' 
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []


t = time.time()
for url in urls:
    thread = threading.Thread(target = fetch_contents, args = (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched in ", time.time() - t, " Second")      # 0.8159351348876953  Second

'''


import threading
from concurrent.futures import ThreadPoolExecutor
import time
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.google.com', 
    'https://www.tensorflow.org/', 
    'https://www.tensorflow.org/install', 
    'https://www.tensorflow.org/tutorials' 
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return (f"Fetched {len(soup.text)} characters from {url}")


t = time.time()

with ThreadPoolExecutor(max_workers = 5) as executor:
    results = executor.map(fetch_contents, urls)

for result in results:
    print(result)


print("All web pages fetched in ", time.time() - t, " Second")     #  0.7742042541503906  Second

