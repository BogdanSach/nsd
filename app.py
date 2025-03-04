def gcd(n, m):
    """Compute the GCD of two integers by Euclid's algorithm."""

    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values.
    while m % n:  # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` amd `m`.
    return n
