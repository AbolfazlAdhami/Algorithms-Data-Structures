def compute_lps(pattern: str) -> list[int]:
    """
    Compute the LPS (longest prefix suffix) array for the pattern.
    lps[i] = length of the longest proper prefix which is also a suffix in pattern[:i+1].
    Time: O(m)
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
                # do not increment i here
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Search for pattern in text using the KMP algorithm.
    Returns a list of starting indices where pattern is found.
    Time: O(n + m)
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    lps = compute_lps(pattern)
    result = []

    i = j = 0  # i->text, j->pattern
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


def main_kmp():
    pattern = input("Enter the pattern: ")
    text = input("Enter the text: ")
    matches = kmp_search(text, pattern)
    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("No match found.")


if __name__ == "__main__":
    main_kmp()
