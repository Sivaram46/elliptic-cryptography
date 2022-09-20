def modular_inverse(a, m):
    # return pow(a, -1, m)
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception(f"Modular inverse doesn't exist for {a} under modulo {m}")
        else:
            return x % m

    return modinv(a, m)

def modular_exp(a, x, m):
    if (a == 0 or a == 1):
        return a
    
    res = 1
    a %= m
    while (x > 0):
        if (x % 2 == 1):
            res = (res * a) % m
        x >>= 1
        a = (a * a) % m
        
    return res