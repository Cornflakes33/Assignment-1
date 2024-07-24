def mortal_fibonacci(n, m):
    rabbits = [1] + [0] * (m - 1)
    for _ in range(n - 1):
        rabbits = [sum(rabbits[1:])] + rabbits[:-1]
    return sum(rabbits)

if __name__ == "__main__":
    n, m = 8, 4
    result = mortal_fibonacci(n, m)
    print(result)