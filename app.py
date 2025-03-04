def gcd(n, m):
    """Compute the GCD of two integers by Euclid's algorithm."""

    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values.
    while m % n:  # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` amd `m`.
    return n


def test_gcd(n, m):
    d = gcd(n, m)

    assert d > 0  # 1) `d` is positive
    assert n % d == 0  # 2) `d` divides `n`
    assert m % d == 0  # 3) `d` divides `m`

    # 4) no other number larger than `d` divides both `n` and `m`
    for i in range(d + 1, min(n, m)):
        assert (n % i) or (m % i)
