import base64
from typing import List

B64 = """AQABAAEAAwEDAQIJBQECAgMBAQK4AwECBgEABAABAAEAAwEDAQLaBQECAgMBAQKSAwECBgEABAABAAEAAwEDAQLwBQECAgMBAQLSAwECBgEABAABAAEAAwEDAQLaBQECAgMBAQKrAwECBgEABAABAAEAAwEDAQLBBQECAgMBAQKHAwECBgEABAABAAEAAwEDAQLuBQECAgMBAQLMAwECBgEABAABAAEAAwEDAQKpBQECAgMBAQL6AwECBgEABAABAAEAAwEDAQLKBQECAgMBAQJ6AwECBgEABAABAAEAAwEDAQK6BQECAgMBAQK/AwECBgEABAABAAEAAwEDAQLQBQECAgMBAQKbAwECBgEABAABAAEAAwEDAQLDBQECAgMBAQLnAwECBgEABAABAAEAAwEDAQKJBQECAgMBAQL+AwECBgEABAABAAEAAwEDAQKNBQECAgMBAQIWAwECBgEABAABAAEAAwEDAQKABQECAgMBAQIjAwECBgEABAABAAEAAwEDAQKABQECAgMBAQJEAwECBgEABAABAAEAAwEDAQJaBQECAgMBAQKtAwECBgEABAABAAEAAwEDAQKhBQECAgMBAQLrAwECBgEABAABAAEAAwEDAQLHBQECAgMBAQJCAwECBgEABAABAAEAAwEDAQJFBQECAgMBAQKaAwECBgEABAABAAEAAwEDAQL5BQECAgMBAQLEAwECBgEABAABAAEAAwEDAQLSBQECAgMBAQKHAwECBgEABAABAAEAAwEDAQKiBQECAgMBAQKDAwECBgEABAABAAEAAwEDAQLyBQECAgMBAQLSAwECBgEABAABAAEAAwEDAQJDBQECAgMBAQI5AwECBgEABAABAAEAAwEDAQIDBQECAgMBAQLNAwECBgEABAABAAEAAwEDAQJPBQECAgMBAQIWAwECBgEABAABAAEAAwEDAQLIBQECAgMBAQJqAwECBgEABAABAAEAAwEDAQJaBQECAgMBAQKvAwECBgEABAABAAEAAwEDAQKYBQECAgMBAQLWAwECBgEABAABAAEAAwEDAQJSBQECAgMBAQI8AwECBgEABAABAAEAAwEDAQK3BQECAgMBAQJsAwECBgEABAABAAEAAwEDAQL9BQECAgMBAQLkAwECBgEABAABAAEAAwEDAQKqBQECAgMBAQIpAwECBgEABAABAAEAAwEDAQLnBQECAgMBAQIjAwECBgEABAABAAEAAwEDAQLGBQECAgMBAQJ9AwECBgEABAABAAEAAwEDAQLiBQECAgMBAQLyAwECBgEABAABAAEAAwEDAQKEBQECAgMBAQIIAwECBgEABAABAAEAAwEDAQJwBQECAgMBAQLTAwECBgEABAABAAEAAwEDAQIrBQECAgMBAQJ1AwECBgEABAABAAEAAwEDAQLrBQECAgMBAQIdAwECBgEABAABBgAA"""
PROGRAM = base64.b64decode(B64)

OP_NAMES = {
    0: "IN",
    1: "IMM",
    2: "MOV",
    3: "ADD",
    4: "MUL",
    5: "XOR",
    6: "NOTZ",
}


def decode_ops(program: bytes):
    for i in range(0, len(program), 3):
        yield i // 3, program[i], program[i + 1], program[i + 2]


def run_with_trace(flag: bytes, max_steps: int = 10_000):
    mem: List[int] = [0] * 256
    ip = 0
    input_pos = 0
    step = 0

    while step < max_steps and 0 <= ip < len(PROGRAM):
        opcode = PROGRAM[ip]
        a = PROGRAM[ip + 1]
        b = PROGRAM[ip + 2]
        ip += 3

        before_a = mem[a]
        before_b = mem[b]
        op_name = OP_NAMES.get(opcode, f"OP{opcode}")

        if opcode == 0:
            if input_pos >= len(flag):
                ch = 0
            else:
                ch = flag[input_pos]
            mem[a] = ch
            detail = f"mem[{a}] = input[{input_pos}] -> {ch} ({chr(ch) if 32 <= ch <= 126 else '.'})"
            input_pos += 1
        elif opcode == 1:
            mem[a] = b
            detail = f"mem[{a}] = {b}"
        elif opcode == 2:
            mem[a] = mem[b]
            detail = f"mem[{a}] = mem[{b}] ({before_b} -> {mem[a]})"
        elif opcode == 3:
            mem[a] = (mem[a] + mem[b]) % 256
            detail = f"mem[{a}] = (mem[{a}] + mem[{b}]) % 256 ({before_a} + {before_b} -> {mem[a]})"
        elif opcode == 4:
            mem[a] = (mem[a] * mem[b]) % 256
            detail = f"mem[{a}] = (mem[{a}] * mem[{b}]) % 256 ({before_a} * {before_b} -> {mem[a]})"
        elif opcode == 5:
            mem[a] = mem[a] ^ mem[b]
            detail = f"mem[{a}] = mem[{a}] ^ mem[{b}] ({before_a} ^ {before_b} -> {mem[a]})"
        elif opcode == 6:
            mem[a] = 0 if mem[a] != 0 else 1
            detail = f"mem[{a}] = 0 if mem[{a}] != 0 else 1 ({before_a} -> {mem[a]})"
        else:
            raise RuntimeError(f"Unknown opcode {opcode} at ip={ip}")

        print(f"step {step:04d} | ip={(ip-3):04d} | {op_name} {a} {b} | {detail}")
        step += 1

    print(f"\n[END] steps={step} mem[0]={mem[0]} input_used={input_pos}")


if __name__ == "__main__":
    flag = b"Alpaca{Futures_Made_of_Virtual_Machines}"
    run_with_trace(flag)
