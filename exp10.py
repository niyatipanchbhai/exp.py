import numpy as np
arr = np.arange(1, 11)

print("Original Array:")
print(arr)

print("\nFirst five elements:")
print(arr[:5])

print("\nLast five elements:")
print(arr[5:])

print("\nElements from index 2 to 6:")
print(arr[2:7])

print("\nAlternate elements:")
print(arr[::2])

print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("\nAdding 5 to every element:")
print(arr + 5)

print("\nMultiplying every element by 2:")
print(arr * 2)

print("\nSubtracting 2 from every element:")
print(arr - 2)
