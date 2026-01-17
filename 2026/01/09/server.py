import os

flag = os.environ.get("FLAG", "Alpaca{*** REDACTED ***}")

inp = input("> ")

# This must be true, isn't it?
if inp == inp.swapcase().swapcase():
    print("Check passed!")
else:
    print("Check failed - !?")
    print("Here is your flag:", flag)
