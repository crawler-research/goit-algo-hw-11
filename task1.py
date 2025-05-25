import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

def run_benchmark():
    sizes = [10_000, 50_000, 100_000, 500_000, 5000_000]
    randomized_times = []
    deterministic_times = []
        
    for size in sizes:
        print(f"Розмір масиву: {size}")
        
        rand_total = 0
        det_total = 0
        
        for _ in range(5):
            arr = [random.randint(1, 1000) for _ in range(size)]
            
            rand_total += measure_time(randomized_quick_sort, arr)
            det_total += measure_time(deterministic_quick_sort, arr)
        
        rand_avg = rand_total / 5
        det_avg = det_total / 5
        
        randomized_times.append(rand_avg)
        deterministic_times.append(det_avg)
        
        print(f"   Рандомізований QuickSort: {rand_avg:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_avg:.4f} секунд")
        print()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_times, marker='s', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('секунди)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*60)
    print("ТАБЛИЦЯ РЕЗУЛЬТАТІВ")
    print("="*60)
    print(f"{'Розмір':<10} {'Рандомізований':<18} {'Детермінований':<18}")
    print("-"*60)
    for i, size in enumerate(sizes):
        print(f"{size:<10} {randomized_times[i]:<18.4f} {deterministic_times[i]:<18.4f}")
    
test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Початковий масив:", test_arr)
print("Рандомізований QuickSort:", randomized_quick_sort(test_arr.copy()))
print("Детермінований QuickSort:", deterministic_quick_sort(test_arr.copy()))
print("\n")

run_benchmark()