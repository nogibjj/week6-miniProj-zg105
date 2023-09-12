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

def get_descriptive_statistics(data):
    stats = {}
    for col in data.columns:
        if data[col].dtype != pl.Object:
            col_stats = {
                "mean": data[col].mean(),
                "median": data[col].median(),
                "std": data[col].std()
            }
            # Only include columns with at least one non-None value
            if any(value is not None for value in col_stats.values()):
                stats[col] = col_stats
    return stats

if __name__ == "__main__":
    data = pl.read_csv("data.csv")
    stats = get_descriptive_statistics(data)
    for col, values in stats.items():
        print(f"Statistics for {col}:")
        for stat, value in values.items():
            print(f"{stat}: {value}")
        print("\n")

    plot_distribution(data)
