import re
import socket

HOST = "34.170.146.252"
PORT = 23793


def make_variants_of_digits(digits: str, allow_plus: bool):
    n = len(digits)
    for mask in range(1 << (n - 1)):
        parts = [digits[0]]
        for i in range(n - 1):
            if (mask >> i) & 1:
                parts.append("_")
            parts.append(digits[i + 1])
        s = "".join(parts)
        yield s
        if allow_plus:
            yield "+" + s


def generate_100_patterns():
    out = []
    seen = set()

    for k in range(0, 30):
        base = "0" * k + "100"
        for cand in make_variants_of_digits(base, allow_plus=True):
            s = cand.strip()
            if not s.isascii():
                continue
            if len(s) > 10:
                continue
            if s in seen:
                continue
            try:
                if int(s) != 100:
                    continue
            except ValueError:
                continue

            seen.add(s)
            out.append(s)
            if len(out) == 100:
                return out

    raise RuntimeError(f"100個作れませんでした: {len(out)}")


def recv_until_prompt(sock: socket.socket, prompt=b"100? ", timeout=5.0):
    sock.settimeout(timeout)
    buf = b""
    while prompt not in buf:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
    return buf


def recv_all(sock: socket.socket, idle_timeout=2.0):
    sock.settimeout(idle_timeout)
    buf = b""
    while True:
        try:
            chunk = sock.recv(4096)
            if not chunk:
                break
            buf += chunk
        except socket.timeout:
            break
    return buf


def main():
    patterns = generate_100_patterns()
    print(f"[*] Generated: {len(patterns)} patterns")

    with socket.create_connection((HOST, PORT), timeout=10) as sock:
        all_recv = b""

        # 最初のプロンプト受信
        data = recv_until_prompt(sock)
        all_recv += data
        if data:
            print(data.decode("utf-8", errors="replace"), end="")

        # 100回、プロンプトごとに送信
        for i, p in enumerate(patterns, 1):
            sock.sendall((p + "\n").encode("ascii"))
            print(f"[{i:03d}/100] sent: {p!r}")

            # 最後以外は次プロンプトまで読む
            if i < 100:
                data = recv_until_prompt(sock)
                all_recv += data
                if data:
                    print(data.decode("utf-8", errors="replace"), end="")

        # 最後の出力(FLAG含む)を回収
        tail = recv_all(sock, idle_timeout=3.0)
        all_recv += tail
        if tail:
            print(tail.decode("utf-8", errors="replace"), end="")

    text = all_recv.decode("utf-8", errors="replace")
    m = re.search(r"Alpaca\{[^}\r\n]*\}", text)
    print("\n===== RESULT =====")
    if m:
        print(f"[+] FLAG: {m.group(0)}")
    else:
        print("[-] FLAG形式は見つかりませんでした（全受信ログは上に表示済み）")


if __name__ == "__main__":
    main()