import re
import sys


asm = """
0x7ffff7fbc002: cmpb $0x41,(%rdi)
0x7ffff7fbc00b: cmpb $0x7d,0x23(%rdi)
0x7ffff7fbc015: cmpb $0x6c,0x1(%rdi)
0x7ffff7fbc01f: cmpb $0x6e,0x10(%rdi)
0x7ffff7fbc029: cmpb $0x63,0x4(%rdi)
0x7ffff7fbc033: cmpb $0x39,0x14(%rdi)
0x7ffff7fbc03d: cmpb $0x61,0x5(%rdi)
0x7ffff7fbc047: cmpb $0x61,0x8(%rdi)
0x7ffff7fbc051: cmpb $0x61,0x17(%rdi)
0x7ffff7fbc05b: cmpb $0x34,0x12(%rdi)
0x7ffff7fbc065: cmpb $0x6e,0x1a(%rdi)
0x7ffff7fbc06f: cmpb $0x77,0x9(%rdi)
0x7ffff7fbc079: cmpb $0x69,0xc(%rdi)
0x7ffff7fbc083: cmpb $0x34,0xa(%rdi)
0x7ffff7fbc08d: cmpb $0x5f,0xd(%rdi)
0x7ffff7fbc097: cmpb $0x69,0xf(%rdi)
0x7ffff7fbc09d: cmpb $0x70,0x1e(%rdi)
0x7ffff7fbc0a3: cmpb $0x6d,0xe(%rdi)
0x7ffff7fbc0a9: cmpb $0x63,0x20(%rdi)
"""


def parse_cmpb_block(text: str) -> list[tuple[int, int]]:
    pairs = []
    pattern = re.compile(
        r"cmpb\s+\$0x([0-9a-fA-F]+),(?:0x([0-9a-fA-F]+))?\(%rdi\)"
    )

    for m in pattern.finditer(text):
        value = int(m.group(1), 16)
        index = int(m.group(2), 16) if m.group(2) is not None else 0
        pairs.append((index, value))

    return pairs


def restore_string(pairs: list[tuple[int, int]]) -> str:
    if not pairs:
        return ""

    max_index = max(index for index, _ in pairs)
    buf = ["?"] * (max_index + 1)

    for index, value in pairs:
        buf[index] = chr(value)

    return "".join(buf)


input_text = sys.stdin.read().strip()
data = parse_cmpb_block(input_text if input_text else asm)
result = restore_string(data)

print(result)