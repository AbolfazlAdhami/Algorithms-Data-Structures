def count_bits(n):
    counter = 0
    while n > 0:
        print(n)
        counter += 1
        n = n >> 1
    return counter


if __name__=='__main__':
        print(bin(16))
        print(count_bits(16))