'''
main function here
'''
import pandas as pd
import matplotlib.pyplot as plt

def func(df):
    return df[df[" \"Score\""] > 100]

if __name__ == "__main__":
    data = pd.read_csv("./data.csv")
    # analyze
    target = data[" \"Score\""]
    print("Mean: ", target.mean())
    print("Median: ", target.median())
    print("Standard Deviation: ", target.std())
    plt.scatter(data["name"], data[" \"Score\""])
    plt.savefig("visualization.png")