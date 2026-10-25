"""
Fibonacci program.

The Fibonacci series starts with 0 and 1, and every next number is the
sum of the previous two:  0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def fibonacci_series(count):
    """Return a list with the first `count` Fibonacci numbers (loop method)."""
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b       # move forward: new a = old b, new b = old a + old b
    return series


def fibonacci_recursive(n):
    """Return the n-th Fibonacci number (0-indexed) using recursion."""
    if n <= 1:                # base cases: fib(0) = 0, fib(1) = 1
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main():
    try:
        count = int(input("How many Fibonacci numbers do you want? "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if count <= 0:
        print("Please enter a number greater than 0.")
        return

    print("Fibonacci series (loop):", fibonacci_series(count))
    print("Fibonacci series (recursion):",
          [fibonacci_recursive(i) for i in range(count)])


if __name__ == "__main__":
    main()
