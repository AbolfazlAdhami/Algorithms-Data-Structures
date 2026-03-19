class ZAlgorithm:
    def __init__(self, pattern: str, text: str) -> None:
        self.pattern = pattern
        self.text = text
        # Use a separator character ('$') that does not appear in pattern or text
        self._concat = f"{pattern}${text}"

    def compute_z_array(self) -> list[int]:
        """
        Compute the Z-array for the concatenated string.
        Z[i] = length of the longest substring starting at i that matches prefix of the string.
        Time complexity: O(N), where N = len(pattern) + 1 + len(text)
        """
        s = self._concat
        n = len(s)
        Z = [0] * n
        l = r = 0  # [l, r] is the current Z-box

        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            # extend the Z-box as far as possible
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            # update the Z-box if we've extended past r
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        return Z

    def search(self) -> list[int]:
        """
        Search for occurrences of pattern in text using the Z-array.
        Returns a list of starting indices in 'text' where 'pattern' is found.
        """
        m = len(self.pattern)
        Z = self.compute_z_array()
        result = []

        # matches start at positions i where Z[i] >= m
        # offset by (m + 1) because of "pattern + '$'"
        offset = m + 1
        for i in range(offset, len(Z)):
            if Z[i] >= m:
                result.append(i - offset)

        return result


if __name__ == "__main__":
    pattern = input("Enter the pattern: ")
    text = input("Enter the text: ")
    zalg = ZAlgorithm(pattern, text)
    matches = zalg.search()

    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("No match found.")
