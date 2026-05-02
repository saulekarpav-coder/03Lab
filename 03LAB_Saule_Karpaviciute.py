
import pandas as pd

df = pd.read_csv("athlete_events.csv").sample(n=50_000, random_state=42)
df.to_csv("athlete_events_sample.csv",index=False)
print(df.shape)
df.head()



df = df.dropna(subset=["ID", "Year", "Weight"])
df["ID"] = df["ID"].astype(int)
df["Year"] = df["Year"].astype(int)
df["Weight"] = df["Weight"].astype(float)

print(df.shape)




#Linear search
def linear_search(arr, key):
    for item in arr:
        if item == key:
            return item
    return None


#Binary Search
def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return None


#Jump Search
import math

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n)-1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None
    
    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return arr[i]
    
    return None


#Interpolation Search
def interpolation_search(arr, key):
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= key <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == key:
                return arr[low]
            return None
        
        pos = low + int(((high - low) / (arr[high] - arr[low])) * (key - arr[low]))
        
        if arr[pos] == key:
            return arr[pos]
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    
    return None

import time
import matplotlib.pyplot as plt

sizes = [1000, 10000, 50000]

results = {
    "Linear": [],
    "Binary": [],
    "Jump": [],
    "Interpolation": []
}

for n in sizes:
    sample = df["ID"].head(n).tolist()
    sample_sorted = sorted(sample)
    key = sample_sorted[n // 2]
    
    # Linear
    times = []
    for _ in range(3):
        start = time.perf_counter()
        linear_search(sample, key)
        times.append((time.perf_counter() - start) * 1000)
    results["Linear"].append(sum(times)/3)
    
    # Binary
    times = []
    for _ in range(3):
        start = time.perf_counter()
        binary_search(sample_sorted, key)
        times.append((time.perf_counter() - start) * 1000)
    results["Binary"].append(sum(times)/3)
    
    # Jump
    times = []
    for _ in range(3):
        start = time.perf_counter()
        jump_search(sample_sorted, key)
        times.append((time.perf_counter() - start) * 1000)
    results["Jump"].append(sum(times)/3)
    
    # Interpolation
    times = []
    for _ in range(3):
        start = time.perf_counter()
        interpolation_search(sample_sorted, key)
        times.append((time.perf_counter() - start) * 1000)
    results["Interpolation"].append(sum(times)/3)

# Plot
for name, vals in results.items():
    plt.plot(sizes, vals, label=name)

plt.xlabel("n")
plt.ylabel("Time (ms)")
plt.title("Search Algorithms Benchmark")
plt.legend()
plt.show()