import requests
import threading
import time

URL = "http://127.0.0.1:5000/recommend/user1"
NUM_USERS = 10

success_count = 0
total_time = 0

def hit_api():
    global success_count, total_time

    start = time.time()
    try:
        res = requests.get(URL)
        print("Status:", res.status_code)

        if res.status_code == 200:
            success_count += 1
    except Exception as e:
        print("Error:", e)

    end = time.time()
    total_time += (end - start)

threads = []

start_test = time.time()

for _ in range(NUM_USERS):
    t = threading.Thread(target=hit_api)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_test = time.time()

# results
print("Load Test Completed")
print("Total Requests:", NUM_USERS)
print("Successful Requests:", success_count)
print("Total Time:", round(end_test - start_test, 4), "sec")
print("Avg Response Time:", round(total_time / NUM_USERS, 4), "sec")