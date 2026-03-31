def partition(arr, low, high):
    partition.cnt += 1
    pivot = arr[high]
    i = low - 1                   
    
    for j in range(low, high):     
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1                  


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    partition.cnt = 0
    quick_sort(arr, 0, N - 1)
    print(partition.cnt)
    print(*arr)