def multiply(a, b):
    result = 0
    while b > 0:

        if b ^ 1 == b-1:
            result = result+a
        a <<= 1
        b >>= 1

    return result


if __name__ == '__main__':
    print(multiply(55, 77))
    print(55 * 77)
