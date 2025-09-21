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