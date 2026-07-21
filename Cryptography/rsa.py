import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q, e=3):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be distinct prime numbers.")
    if p == q:
        raise ValueError("p and q must be distinct.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if math.gcd(e, phi) != 1:
        raise ValueError(f"e={e} is not coprime to phi={phi}")
        
    d = modinv(e, phi)
    return ((e, n), (d, n), phi)

def encrypt(public_key, plaintext_num):
    e, n = public_key
    if not (0 <= plaintext_num < n):
        raise ValueError("Message m must satisfy 0 <= m < n")
    return pow(plaintext_num, e, n)

def decrypt(private_key, ciphertext):
    d, n = private_key
    return pow(ciphertext, d, n)

def run_test_case(p, q, e, m):
    print(f"\n--- Testing RSA with p={p}, q={q}, e={e}, m={m} ---")
    pub, priv, phi = generate_keypair(p, q, e)
    print(f"p={p}, q={q}")
    print(f"n = p*q = {pub[1]}")
    print(f"phi(n) = (p-1)*(q-1) = {phi}")
    print(f"Public Key (e, n): {pub}")
    print(f"Private Key (d, n): {priv}")
    
    c = encrypt(pub, m)
    print(f"Encrypted message c = m^e mod n: {c}")
    
    decrypted_m = decrypt(priv, c)
    print(f"Decrypted message m' = c^d mod n: {decrypted_m}")
    
    assert m == decrypted_m, "Decryption failed!"
    print("SUCCESS: Decrypted message matches original message.")

if __name__ == "__main__":
    # Test Case 1 (Worked Example)
    run_test_case(p=3, q=11, e=3, m=4)
    
    # Test Case 2 (Additional Example)
    run_test_case(p=13, q=17, e=5, m=42)
