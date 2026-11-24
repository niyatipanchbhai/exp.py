import pandas as pd
import numpy as np

data = np.random.randint(1, 100, 10)

s = pd.Series(data)

print("Original Series:")
print(s)

print("\nElement at index 3:")
print(s[3])

print("\nFirst five elements:")
print(s[:5])

print("\nNumbers greater than 50:")
print(s[s > 50])

print("\nNumbers less than 30:")
print(s[s < 30])

print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
print("Sum:", s.sum())
