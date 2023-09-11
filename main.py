'''
main function here
'''
import pandas as pd
import matplotlib.pyplot as plt

def data_filter(df):
    return df[df[" \"Final\""] >= 100]

if __name__ == "__main__":
    dataframe = pd.read_csv("./data.csv")
    # analyze
    target = dataframe[" \"Final\""]
    print("Mean: ", target.mean())
    print("Median: ", target.median())
    print("Standard Deviation: ", target.std())
    plt.scatter(dataframe["name"], dataframe[" \"Final\""])
    plt.savefig("visualization.png")