class RabinKarp:
    def __init__(self, pattern: str, text: str):
        self.pattern = pattern
        self.text = text
        # Size of the alphabet (number of possible character values)
        self.d = 256
        # A prime modulus for the rolling hash
        self.q = 101

    def search(self) -> None:
        m = len(self.pattern)
        n = len(self.text)
        if m > n:
            print("Pattern is longer than text. No match.")
            return

        # Compute the high-order digit multiplier h = (d^(m-1)) % q
        h = pow(self.d, m - 1, self.q)

        # Initial hash values for pattern and first window of text
        hash_p = 0
        hash_t = 0
        for i in range(m):
            hash_p = (self.d * hash_p + ord(self.pattern[i])) % self.q
            hash_t = (self.d * hash_t + ord(self.text[i])) % self.q

        # Slide the pattern over text one by one
        for i in range(n - m + 1):
            # If the hash values match, verify by direct string comparison
            if hash_p == hash_t:
                if self.text[i: i + m] == self.pattern:
                    print(f"Found match at index {i}")

            # Compute hash for the next window of text:
            # Remove leading char, add trailing char
            if i < n - m:
                hash_t = (
                    (self.d * (hash_t - ord(self.text[i]) * h)
                     + ord(self.text[i + m]))
                    % self.q
                )
                # Ensure positive
                if hash_t < 0:
                    hash_t += self.q


def main():
    pattern = input("Enter the pattern to search for: ")
    text = input("Enter the text: ")
    rk = RabinKarp(pattern, text)
    rk.search()


if __name__ == "__main__":
    main()
