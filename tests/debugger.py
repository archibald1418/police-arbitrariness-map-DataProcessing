
def factorial(a: int) -> int:
    if a < 2:
        return 0
    else:
        return a * factorial(a - 1)


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(5))
    print(factorial(-1))