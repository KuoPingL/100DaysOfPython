import time

class RLock:
    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit")


lock = RLock()

with lock:
    print("Something")
    time.sleep(2)

# lock = "abc"
#
# with lock:
#     print("This")