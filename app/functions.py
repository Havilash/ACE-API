

def celsius_to_kelvin(celsius):
    return 273.15 + celsius

def primes(limit):
    isPrime = [True] * (limit+1)

    for i in range(2, limit+1):
        if isPrime[i]:
            for j in range(i*2, limit+1, i):
                isPrime[j] = False

    return [i for i in range(2, limit+1) if isPrime[i]]

def fibonacci_recursive(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print(a, b)
    return a
