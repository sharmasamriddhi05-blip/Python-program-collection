"""
Factorial program.

The factorial of a number n (written n!) is n x (n-1) x (n-2) x ... x 1.
Example: 5! = 5 x 4 x 3 x 2 x 1 = 120
By definition, 0! = 1.
"""


def factorial_loop(n):
    """Find the factorial using a loop."""
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def factorial_recursive(n):
    """Find the factorial using recursion (a function calling itself)."""
    if n == 0 or n == 1:      # base case: stops the recursion
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        number = int(input("Enter a non-negative whole number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    print(f"Factorial of {number} (loop):      {factorial_loop(number)}")
    print(f"Factorial of {number} (recursion): {factorial_recursive(number)}")


if __name__ == "__main__":
    main()
