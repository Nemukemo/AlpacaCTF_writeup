import base64
import zlib

cookie_header = ".eJwlyzELwjAQhuG_cmRxcagUEbqJk6uDk3Cc5msNxlzJGaWU_ncjbi8PvLN7wkwGuM6d1GAkGZTh15d0Dhrx-ss1FlQ6rt6ge_AeiYT6KEO1X9bTgibqNdOkpaN9HOUm80GbxwbGklu2D9odS_K81QrgqSmLW77kUS59.ac5mQQ.QieONI4T1KFtPXd_bB5bUkbU_KY;"

# session値だけ抽出（"session=...;" でも生値でも対応）
def extract_session_value(cookie_text: str) -> str:
    s = cookie_text.strip()
    if "session=" in s:
        return s.split("session=", 1)[1].split(";", 1)[0].strip()
    return s.rstrip(";").strip()


v = extract_session_value(cookie_header)

# Flaskセッション形式: ".<payload>.<ts>.<sig>" のことがある
parts = v.split(".")
payload_b64 = parts[1] if parts[0] == "" else parts[0]

# base64url のパディング補正
payload_b64 += "=" * (-len(payload_b64) % 4)

raw = base64.urlsafe_b64decode(payload_b64)

# 圧縮されていれば展開、されてなければそのまま
try:
    raw = zlib.decompress(raw)
except zlib.error:
    pass

print(raw.decode("utf-8", errors="replace"))