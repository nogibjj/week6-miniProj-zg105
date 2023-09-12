'''
main function here
'''
import polars as pl
import matplotlib.pyplot as plt

def plot_distribution(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data["grades"].to_numpy(), bins=10, edgecolor="k", alpha=0.7)
    plt.title(f"Distribution of grades")
    plt.xlabel("grades)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"grades_distribution.png")
    plt.show()

def analyze(data):
    res = {}
    col_stats = {
        "mean": data["grades"].mean(),
        "median": data["grades"].median(),
        "std": data["grades"].std()
    }
    res["grades"] = col_stats
    return res

if __name__ == "__main__":
    data = pl.read_csv("data.csv")
    res = analyze(data)
    for col, values in res.items():
        print(f"Statistics for {col}:")
        for stat, value in values.items():
            print(f"{stat}: {value}")
        print("\n")

    plot_distribution(data)
