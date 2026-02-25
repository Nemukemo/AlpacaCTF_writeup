import os
from random import randint

flag = int.from_bytes(os.getenv("FLAG", "Alpaca{REDACTED}").encode(), "big")
print(flag * randint(2, 2026) * randint(2, 2026) * randint(2, 2026))
print(flag * randint(2, 2026) * randint(2, 2026) * randint(2, 2026))
