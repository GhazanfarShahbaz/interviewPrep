def recursiveMultiply(first: int, second: int) -> int:
    if first > second:
        return multiply(second, first)
    return multiply(first, second)


def multiply(number, other):
    if number == 0:
        return 0
    elif number == 1:
        return other

    s = number//2

    middle = multiply(s, other)

    if number % 2 == 0:
        return middle + middle
    else:
        return middle + middle + other


if __name__ == "__main__":
    print(recursiveMultiply(4, 6))