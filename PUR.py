import multiprocessing
import requests
import time
import random
from multiprocessing import Process
from fake_useragent import UserAgent
import sys

proxx = subprocess.Popen('curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt > proxy.txt', stdout=subprocess.PIPE, shell=True).communicate()
import random
f = open("proxy.txt", "r")
lines = f.readlines()
def random_line(afile):     
    line = random.choice(lines)
    return line.strip()

def proxiess():
    while True:
        ex = str(random_line(f))
        proxies = {
                'http': 'http://'+ex,
            }
        return proxies

user_agents = UserAgent()

proxies = proxiess()

search_string = sys.argv[1]

def send_request(url):
    try:
        # rate limit of 10 requests per minute
        time.sleep(6)
        headers = {"User-Agent": user_agents}
        proxy = random.choice(proxies)
        response = requests.get(url, headers=headers, proxies=proxy)
        if re.search(search_string, response.text):
            print(f"[+] Found {search_string} in {url}")
        else:
            print(f"[-] {search_string} not found in {url}")
            print(f"[+] Got response from {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Request error: {e}")

    

        
processes = []

for url in urls:
    p = Process(target=send_request, args=(url,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("[+] All requests sent.")
