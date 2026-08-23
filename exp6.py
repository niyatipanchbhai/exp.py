def fibonacci(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


n = int(input("Enter n: "))

if n < 0:
    print("Fibonacci number is not defined for negative numbers.")
else:
    print(f"The {n}th Fibonacci number is:", fibonacci(n))