def fibonacci(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a * k + b
        return b

if __name__ == "__main__":
    n, k = 6, 4
    result = fibonacci(n, k)
    print(result)