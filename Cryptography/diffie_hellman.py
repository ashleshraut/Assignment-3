def is_primitive_root(g, p):
    # Basic check for small prime test cases
    required_set = {num for num in range(1, p)}
    actual_set = {pow(g, powers, p) for powers in range(1, p)}
    return required_set == actual_set

def run_dh_exchange(p, g, a, b):
    print(f"\n--- Running Diffie-Hellman Exchange (p={p}, g={g}, a={a}, b={b}) ---")
    if not is_primitive_root(g, p):
        raise ValueError(f"g={g} is not a primitive root modulo p={p}")
    
    if not (1 <= a < p - 1) or not (1 <= b < p - 1):
        raise ValueError("Private keys must satisfy 1 <= key < p - 1")
        
    # Alice computes A = g^a mod p
    A = pow(g, a, p)
    # Bob computes B = g^b mod p
    B = pow(g, b, p)
    
    print(f"Alice Public Exchange Value A: {A}")
    print(f"Bob Public Exchange Value B:   {B}")
    
    # Shared secret computation
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)
    
    print(f"Alice Computed Shared Secret K: {K_alice}")
    print(f"Bob Computed Shared Secret K:   {K_bob}")
    
    assert K_alice == K_bob, "Shared secrets do not match!"
    print("SUCCESS: Both parties computed identical shared key.")

if __name__ == "__main__":
    # Worked Example: p=29, g=2, a=5, b=12
    run_dh_exchange(p=29, g=2, a=5, b=12)
    
    # Additional Example: p=23, g=5, a=6, b=15
    run_dh_exchange(p=23, g=5, a=6, b=15)
