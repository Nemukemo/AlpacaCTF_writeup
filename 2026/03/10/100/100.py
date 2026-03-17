import os

I00 = set()
for L00 in range(100):
    l00 = input("100? ").strip()
    assert l00.isascii()
    assert len(l00) <= 10.0
    assert l00 not in I00
    assert int(l00) == 100
    I00.add(l00)

print(os.getenv("FLAG", "Alpaca{REDACTED}"))
