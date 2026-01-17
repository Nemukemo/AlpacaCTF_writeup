import base64
from z3 import BitVec, BitVecVal, If, Solver, sat

b64 = """AQABAAEAAwEDAQIJBQECAgMBAQK4AwECBgEABAABAAEAAwEDAQLaBQECAgMBAQKSAwECBgEABAABAAEAAwEDAQLwBQECAgMBAQLSAwECBgEABAABAAEAAwEDAQLaBQECAgMBAQKrAwECBgEABAABAAEAAwEDAQLBBQECAgMBAQKHAwECBgEABAABAAEAAwEDAQLuBQECAgMBAQLMAwECBgEABAABAAEAAwEDAQKpBQECAgMBAQL6AwECBgEABAABAAEAAwEDAQLKBQECAgMBAQJ6AwECBgEABAABAAEAAwEDAQK6BQECAgMBAQK/AwECBgEABAABAAEAAwEDAQLQBQECAgMBAQKbAwECBgEABAABAAEAAwEDAQLDBQECAgMBAQLnAwECBgEABAABAAEAAwEDAQKJBQECAgMBAQL+AwECBgEABAABAAEAAwEDAQKNBQECAgMBAQIWAwECBgEABAABAAEAAwEDAQKABQECAgMBAQIjAwECBgEABAABAAEAAwEDAQKABQECAgMBAQJEAwECBgEABAABAAEAAwEDAQJaBQECAgMBAQKtAwECBgEABAABAAEAAwEDAQKhBQECAgMBAQLrAwECBgEABAABAAEAAwEDAQLHBQECAgMBAQJCAwECBgEABAABAAEAAwEDAQJFBQECAgMBAQKaAwECBgEABAABAAEAAwEDAQL5BQECAgMBAQLEAwECBgEABAABAAEAAwEDAQLSBQECAgMBAQKHAwECBgEABAABAAEAAwEDAQKiBQECAgMBAQKDAwECBgEABAABAAEAAwEDAQLyBQECAgMBAQLSAwECBgEABAABAAEAAwEDAQJDBQECAgMBAQI5AwECBgEABAABAAEAAwEDAQIDBQECAgMBAQLNAwECBgEABAABAAEAAwEDAQJPBQECAgMBAQIWAwECBgEABAABAAEAAwEDAQLIBQECAgMBAQJqAwECBgEABAABAAEAAwEDAQJaBQECAgMBAQKvAwECBgEABAABAAEAAwEDAQKYBQECAgMBAQLWAwECBgEABAABAAEAAwEDAQJSBQECAgMBAQI8AwECBgEABAABAAEAAwEDAQK3BQECAgMBAQJsAwECBgEABAABAAEAAwEDAQL9BQECAgMBAQLkAwECBgEABAABAAEAAwEDAQKqBQECAgMBAQIpAwECBgEABAABAAEAAwEDAQLnBQECAgMBAQIjAwECBgEABAABAAEAAwEDAQLGBQECAgMBAQJ9AwECBgEABAABAAEAAwEDAQLiBQECAgMBAQLyAwECBgEABAABAAEAAwEDAQKEBQECAgMBAQIIAwECBgEABAABAAEAAwEDAQJwBQECAgMBAQLTAwECBgEABAABAAEAAwEDAQIrBQECAgMBAQJ1AwECBgEABAABAAEAAwEDAQLrBQECAgMBAQIdAwECBgEABAABBgAA"""
program = base64.b64decode(b64)

# 命令列の解析
ops = []
for i in range(0, len(program), 3):
    ops.append((program[i], program[i+1], program[i+2]))

# 入力変数の用意（opcode==0 の回数だけ）
input_idxs = [i for i,(op,_,_) in enumerate(ops) if op == 0]
inputs = [BitVec(f'c{i}', 8) for i in range(len(input_idxs))]

# メモリ（BitVec 8bit）
mem = [BitVecVal(0, 8) for _ in range(256)]

solver = Solver()

# 任意：入力を printable ASCII に制限（不要なら外してOK）
for c in inputs:
    solver.add(c >= 0x20, c <= 0x7e)

inp_ptr = 0
for op, a, b in ops:
    if op == 0:
        mem[a] = inputs[inp_ptr]
        inp_ptr += 1
    elif op == 1:
        mem[a] = BitVecVal(b, 8)
    elif op == 2:
        mem[a] = mem[b]
    elif op == 3:
        mem[a] = mem[a] + mem[b]
    elif op == 4:
        mem[a] = mem[a] * mem[b]
    elif op == 5:
        mem[a] = mem[a] ^ mem[b]
    elif op == 6:
        mem[a] = If(mem[a] != 0, BitVecVal(0, 8), BitVecVal(1, 8))
    else:
        raise RuntimeError("unknown opcode")

# クリア条件
solver.add(mem[0] == 0)

if solver.check() == sat:
    m = solver.model()
    flag = bytes([m[c].as_long() for c in inputs])
    print(flag.decode(errors="replace"))
else:
    print("No solution.")