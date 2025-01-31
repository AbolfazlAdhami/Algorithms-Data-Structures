from itertools import islice


class Primes:
    def __init__(self):
        self.primes = [2]
        self.num = 3

    @staticmethod
    def stream():
        yield 2  # First prime number
        while True:
            is_prime = True
            for prime in self.primes:
                if prime * prime > self.num:
                    break
                if self.num % prime == 0:
                    is_prime = False
                    break

            if is_prime:
                self.primes.append(self.num)
                yield self.num

            self.num += 2  # Skip even numbers


prime_list = Primes()
print(prime_list.primes)
