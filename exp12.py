import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print("First Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

for col in df.columns:

    if df[col].dtype == 'object':

        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    else:

        df[col] = df[col].fillna(
            df[col].median()
        )

df.drop_duplicates(inplace=True)

print("\nData After Cleaning:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nDataset Shape:")
print(df.shape)

if 'Churn' in df.columns:

    print("\nCustomer Churn Count:")
    print(df['Churn'].value_counts())

    df['Churn'].value_counts().plot(
        kind='bar',
        title='Customer Churn Distribution'
    )

    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.show()

numeric_cols = df.select_dtypes(
    include=np.number
).columns
print("\nCorrelation:")
print(df[numeric_cols].corr())

df[numeric_cols].hist(figsize=(10, 8))

plt.suptitle("Numerical Data Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))

plt.imshow(
    df[numeric_cols].corr(),
    cmap='coolwarm'
)

plt.colorbar()

plt.xticks(
    range(len(numeric_cols)),
    numeric_cols,
    rotation=45
)

plt.yticks(
    range(len(numeric_cols)),
    numeric_cols
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nEDA Completed Successfully!")
