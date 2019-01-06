import sys
from random import randrange
# Import for testing and for runing is different
try:
    from helper import generate_prime_number, extended_gcd
except ImportError:
    from src.helper import generate_prime_number, extended_gcd


def rsa_key_gen(user_seed):
    """ Generate RSA keypair with addtional p, q such that p * q = n
        Args:
            user_seed int: optional argument seed value
        return n, e, d, p, q
    """
    p = generate_prime_number(user_seed)
    q = generate_prime_number(user_seed//2)
    n = p*q
    phi_n = (p-1)*(q-1)

    e = randrange(2, phi_n)
    while extended_gcd(e, phi_n)[0] != 1:
        e = randrange(2, phi_n)
    _, d, _ = extended_gcd(e, phi_n)
    d %= phi_n
    return n, e, d, p, q


if __name__ == "__main__":
    user_seed = randrange(0, 9999999999)
    if len(sys.argv) > 1:
        user_seed = int(sys.argv[1])

    n, e, d, p, q = rsa_key_gen(user_seed)
    print("===============ENCRYPT KEY================")
    print("e:", e)
    print("===============DECRYPT KEY================")
    print("d:", d)
