def risl(c):
    if c.isalpha():
        return (bytes([0xF0, 0x9F, 0x87, 0xA6 + ord(c.upper()) - ord("A")])).decode()
    else:
        return c


def map_risl(s):
    return "".join(map(risl, s))


FLAG = "Alpaca{******}"

print(map_risl(FLAG))
