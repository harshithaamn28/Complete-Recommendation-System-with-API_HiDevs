import requests
import threading
import time

URL = "http://127.0.0.1:5000/recommend/user1"

success_count = 0

start = time.time()


def hit_api():

    global success_count

    try:

        response = requests.get(URL)

        if response.status_code == 200:
            success_count += 1

    except Exception as e:

        print(f"Request failed: {e}")


threads = []

# simulate 10 concurrent users
for _ in range(10):

    t = threading.Thread(target=hit_api)

    threads.append(t)

    t.start()

for t in threads:
    t.join()

end = time.time()

print("Load Test Report")
print("----------------")

print(f"Successful Requests: {success_count}/10")

print(
    f"Total Time: "
    f"{round(end - start, 4)} seconds"
)