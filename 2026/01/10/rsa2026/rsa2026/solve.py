
import sys
from Crypto.Util.number import isPrime, long_to_bytes, inverse

# Increase integer string conversion limit for large numbers
sys.set_int_max_str_digits(100000)

# Read values from output.txt
def read_output():
    with open("output.txt", "r") as f:
        lines = f.readlines()
        n = int(lines[0].split("=")[1].strip())
        e = int(lines[1].split("=")[1].strip())
        c = int(lines[2].split("=")[1].strip())
    return n, e, c

def solve():
    n, e, c = read_output()

    # 1. Generate primes up to 2026
    small_primes = [x for x in range(2026) if isPrime(x)]

    # 2. Factorize n
    # n = p1^k1 * p2^k2 * ...
    factors = {}
    temp_n = n
    
    print("Factorizing n...")
    for p in small_primes:
        if temp_n % p == 0:
            count = 0
            while temp_n % p == 0:
                count += 1
                temp_n //= p
            factors[p] = count
    
    if temp_n != 1:
        print("Warning: n was not fully factorized by primes < 2026")
    
    # 3. Compute phi(n)
    # phi(p^k) = p^k - p^(k-1)
    # phi(n) = product(phi(p^k))
    phi = 1
    for p, k in factors.items():
        phi_pk = (p**k) - (p**(k-1))
        phi *= phi_pk
    
    print(f"Phi calculated.")

    # 4. Compute d
    d = inverse(e, phi)
    
    # 5. Decrypt
    m = pow(c, d, n)
    
    # 6. Convert to bytes
    flag = long_to_bytes(m)
    print(f"Flag found: {flag.decode()}")

if __name__ == "__main__":
    solve()
