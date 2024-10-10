import numpy as np
import time

def create_list_matrix():
    return [[0] * 1501 for _ in range(1501)]

def create_numpy_matrix():
    return np.zeros((1501,1501), dtype=int)

def measure_time(func, repeat=100):
    start_time = time.perf_counter()
    for _ in range(repeat):
        func()
    end_time = time.perf_counter()
    return (end_time - start_time) / repeat

# リスト内包表記での実行時間計測
list_time = measure_time(create_list_matrix)
print(f"リスト内包表記での平均実行時間: {list_time:.6f} 秒")

# NumPyでの実行時間計測
numpy_time = measure_time(create_numpy_matrix)
print(f"NumPyでの平均実行時間: {numpy_time:.6f} 秒")

# 比較結果
if numpy_time > 0:
    print(f"リスト内包表記はNumPyの {list_time/numpy_time:.2f} 倍の時間がかかります")
else:
    print("NumPyの実行時間が測定不能なほど短いため、正確な比較ができません")