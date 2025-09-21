import time # O(1)
import random  # O(1)
import matplotlib.pyplot as plt # O(1)
import timeit


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



# Характеристики ПК (замени на свои реальные)
pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-1135G7 @ 2.40GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.11.6
"""


print(pc_info)
# Проведение экспериментов
sizes = [1000, 5000, 10000, 50000, 100000, 200000]  # Размеры массивов
linear_times = []
binary_times = []

print("Замеры времени выполнения поиска:")
print("{:>10} {:>15} {:>15} {:>15} {:>15}".format(
    "Размер (N)", "Linear (мс)", "Linear/N (мкс)", "Binary (мс)", "Binary/logN (мкс)"
))

for size in sizes:
    arr = list(range(size))
    target = random.choice([0, size // 2, size - 1, size + 1])  # цель поиска

    # Линейный поиск (усредняем по 10 замерам)
    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=10) * 1000 / 10
    linear_times.append(linear_time)
    time_per_element = (linear_time * 1000) / size if size > 0 else 0  # мкс на элемент

    # Бинарный поиск (усредняем по 10 замерам)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=10) * 1000 / 10
    binary_times.append(binary_time)
    time_per_log = (binary_time * 1000) / (size.bit_length())  # мкс на logN

    print("{:>10} {:>15.4f} {:>15.4f} {:>15.4f} {:>15.4f}".format(
        size, linear_time, time_per_element, binary_time, time_per_log
    ))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, 'bo-', label='Линейный поиск O(N)')
plt.plot(sizes, binary_times, 'ro-', label='Бинарный поиск O(log N)')
plt.xlabel('Размер массива (N)')
plt.ylabel('Время выполнения (мс)')
plt.title('Сравнение времени выполнения линейного и бинарного поиска')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('search_time_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Дополнительный анализ
print("\nАнализ результатов:")
print("1. Теоретическая сложность линейного поиска: O(N)")
print("2. Теоретическая сложность бинарного поиска: O(log N)")
print("3. Практические замеры показывают, что бинарный поиск намного быстрее на больших N.")
print("4. Время линейного поиска растёт пропорционально N, а бинарного — примерно как log N.")

