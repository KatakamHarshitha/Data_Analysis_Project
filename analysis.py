import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Display first 5 rows
print(df.head())

# Dataset information
df.info()   # <-- changed from print(df.info())

# Summary statistics
print(df.describe())

# Average sepal length
avg = df["sepal_length"].mean()

print("\nAverage Sepal Length:")
print(avg)

# Print column names (optional)
print(df.columns)

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(8,5))

df["species"].value_counts().plot(kind="bar")

plt.title("Flower Species Count")
plt.xlabel("Species")
plt.ylabel("Count")

plt.savefig("charts/bar_chart.png")

plt.show()

# -----------------------------
# SCATTER PLOT
# -----------------------------
plt.figure(figsize=(8,5))

plt.scatter(
    df["sepal_length"],
    df["petal_length"]
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.savefig("charts/scatter_plot.png")

plt.show()

# -----------------------------
# HEATMAP
# -----------------------------
plt.figure(figsize=(8,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("charts/heatmap.png")

plt.show()
