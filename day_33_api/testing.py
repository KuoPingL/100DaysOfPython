class RLock:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


lock = RLock()

with lock:
    print("Something")

# lock = "abc"
#
# with lock:
#     print("This")