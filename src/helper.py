from random import randrange, getrandbits, seed


def is_prime(n, k=128):
    """ Test if a number is a prime use Miller-Rabin algorithm
        Args:
            n int: number to test
            k int: number of test to do
        return True if n is prime
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n-1)
        x = pow(a, r, n)
        if x != 1 and x != n-1:
            j = 1
            while j < s and x != n-1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n-1:
                return False
        return True


def generate_prime_cadidate(length):
    """ Generate an odd integer randomly
        Args:
            length int: number of bits length
        return a integer
    """
    p = getrandbits(length)
    p |= (1 << length-1) | 1
    return p


def generate_prime_number(user_seed, length=1024):
    """ Generate a prime
        Args:
            user_seed: seed use for randomization
            length int: length of the prime to generate, int bits (default is 1024)
        return a prime number with high properbility
    """
    seed(user_seed)
    p = generate_prime_cadidate(length)
    # keep generating while the primality test fail
    while not is_prime(p, 10):
        p = generate_prime_cadidate(length)
    return p


def extended_gcd(a, b):
    """ Find x, y such that ax+by=gcd(a,b)
        Args:
            a int: first number
            b int: second number
        return gcd, x, y
    """
    xa, ya = 1, 0
    xb, yb = 0, 1
    while b != 0:
        q = a//b
        r = a % b
        a, b = b, r
        xr, yr = xa-q*xb, ya-q*yb
        xa, ya = xb, yb
        xb, yb = xr, yr
    return a, xa, ya
