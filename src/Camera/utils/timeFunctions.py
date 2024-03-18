import time

def countdown(delay: int=5, message: str="") -> None:
    for k in range(delay):
        print(f"{message} ... {delay-k}s remaining", end="\r")
        time.sleep(1)
    print(f"{message} ... {delay-delay}s remaining", end="\r")
    print("\n")
    return

def currentTime():
    return time.time()

