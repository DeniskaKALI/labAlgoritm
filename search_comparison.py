import time # O(1)
import random  # O(1)
import matplotlib.pyplot as plt # O(1)


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

def binary_search(arr, target):
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
    # Общая сложность: O(log n)

def measure_time(func, arr, target, repeat=5):
    """
    Замеряет среднее время выполнения функции поиска.
    """
    start = time.perf_counter()  # O(1)
    for _ in range(repeat):  # O(repeat)
        func(arr, target)  # O(n) или O(log n)
    end = time.perf_counter()  # O(1)
    return (end - start) / repeat  # O(1)


def run_experiments():
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]  # O(1)
    linear_times = []  # O(1)
    binary_times = []  # O(1)

    for size in sizes:  # O(len(sizes))
        arr = list(range(size))  # O(n)
        target = random.choice([0, size // 2, size - 1, size + 1])  # O(1)

        t_linear = measure_time(linear_search, arr, target)  # O(n)
        t_binary = measure_time(binary_search, arr, target)  # O(log n)

        linear_times.append(t_linear)  # O(1)
        binary_times.append(t_binary)  # O(1)

        print(f"Размер: {size}, Linear: {t_linear:.6f}, Binary: {t_binary:.6f}")

    # Построение графика в линейном масштабе
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, linear_times, label="Линейный поиск (O(n))")
    plt.plot(sizes, binary_times, label="Бинарный поиск (O(log n))")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек.)")
    plt.title("Сравнение линейного и бинарного поиска")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Построение графика в логарифмическом масштабе
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, linear_times, label="Линейный поиск (O(n))")
    plt.plot(sizes, binary_times, label="Бинарный поиск (O(log n))")
    plt.xlabel("Размер массива (log scale)")
    plt.ylabel("Время (сек., log scale)")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("Сравнение в логарифмическом масштабе")
    plt.legend()
    plt.grid(True, which="both")
    plt.show()


# Характеристики ПК (замени на свои реальные)
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-1135G7 @ 2.40GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.11.6
"""


print(pc_info)
run_experiments()

