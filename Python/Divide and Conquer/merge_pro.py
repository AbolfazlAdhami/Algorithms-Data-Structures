def merge(low, mid, high, s):
    merge.cnt += 1
    c = [0] * (high - low + 1)
    i = low
    j = mid + 1
    k = 0

    while i <= mid and j <= high:
        if s[i] < s[j]:
            c[k] = s[i]
            i += 1
        else:
            c[k] = s[j]
            j += 1
        k += 1

    while i <= mid:
        c[k] = s[i]
        i += 1
        k += 1

    while j <= high:
        c[k] = s[j]
        j += 1
        k += 1

    # کپی کردن نتیجه مرتب‌شده به آرایه اصلی
    for idx in range(low, high + 1):
        s[idx] = c[idx - low]


def mergesort(low, high, s):
    if low >= high:
        return          # پایه ریکورسیون درست

    mid = (low + high) // 2
    mergesort(low, mid, s)
    mergesort(mid + 1, high, s)   # توجه: mid+1 مهم است!
    merge(low, mid, high, s)


if __name__ == "__main__":
    merge.cnt = 0
    n = int(input())
    s = list(map(int, input().split()))

    mergesort(0, n-1, s)

    print(merge.cnt)
    print(*s)
