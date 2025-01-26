def even_gray_code(size, position):
    def count_bits_diff(a, b):
        return bin(a ^ b).count('1')

    total_elements = 2**size
    visited = set()
    sequence = []
    current = 0
    for _ in range(total_elements):
        sequence.append(current)
        visited.add(current)
        for next_val in range(total_elements):
            if next_val not in visited and count_bits_diff(current, next_val) % 2 == 0:
                current = next_val
                break
    return format(sequence[position], f'0{size}b')


 
print(even_gray_code(4, 5))  # Output: '1010'


print(even_gray_code(2, 0))
