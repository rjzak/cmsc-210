import pandas


def get_dataframe():
    return pandas.read_csv("notebooks/weight-height.csv", header=0)


def print_summary(df):
    summary = df.describe()
    # The median is missing, so let's add it:
    mean = "median    {}    {}".format(round(df.median().Height, 6), round(df.median().Weight, 6))
    print(summary)
    print(mean)


def convert_to_feet(df):
    df.Height = df.Height / 12





