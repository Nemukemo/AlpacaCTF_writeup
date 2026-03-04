import time

flag = "Alpaca{????}"
assert len(flag) == 12

for i, c in enumerate(flag):
    print(c, end="", flush=True)
    time.sleep(i)
