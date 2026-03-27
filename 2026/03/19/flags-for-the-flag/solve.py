from pathlib import Path

# Unicode code point range for regional indicator symbols (A-Z).
REGIONAL_A = 0x1F1E6
REGIONAL_Z = 0x1F1FF


def decode_regional_indicators(text: str) -> str:
    decoded = []
    for ch in text:
        code = ord(ch)
        if REGIONAL_A <= code <= REGIONAL_Z:
            decoded.append(chr(ord("A") + (code - REGIONAL_A)))
        else:
            decoded.append(ch)
    return "".join(decoded)


def main() -> None:
    output_path = Path(__file__).with_name("output.txt")
    encoded = output_path.read_text(encoding="utf-8").strip()
    print(decode_regional_indicators(encoded))


if __name__ == "__main__":
    main()
