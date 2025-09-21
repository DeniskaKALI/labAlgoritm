import time

def linear_search(arr, target):
    """
    Линейный поиск элемента в массиве.
    Сложность: O(N).
    """
    for i in range(len(arr)):  # O(N)
        if arr[i] == target:   # O(1)
            return i           # O(1)
    return -1                  # O(1)
    # Общая сложность: O(N)
test_arr = [10, 20, 30, 40, 50]
print("Тест линейного поиска:")
print(linear_search(test_arr, 30))  # ожидается 2
print(linear_search(test_arr, 50))  # ожидается 4
print(linear_search(test_arr, 99))  # ожидается -1

def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    Сложность: O(log n)
    """
    left, right = 0, len(arr) - 1  # O(1)
    while left <= right:           # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:     # O(1)
            return mid
        elif arr[mid] < target:    # O(1)
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search(test_arr, 30))  # ожидается 2
print(binary_search(test_arr, 50))  # ожидается 4
print(binary_search(test_arr, 99))  # ожидается -1

def measure_time(func, arr, target, repeat=5):
    """
    Замеряет среднее время выполнения функции поиска.
    """
    start = time.perf_counter()  # O(1)
    for _ in range(repeat):  # O(repeat)
        func(arr, target)  # O(n) или O(log n)
    end = time.perf_counter()  # O(1)
    return (end - start) / repeat  # O(1)
