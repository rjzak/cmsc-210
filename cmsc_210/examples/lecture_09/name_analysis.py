import csv

import seaborn

"""
In a given year:

    * What is the most popular name?
    * What is the rank for any given name?

Across a period of years?

    * How has the popularity of a name changed?
    * How do we measure "popular," anyway?

"""


def get_year(year):
    filename = f"names/yob{year}.txt"
    female_data = []
    male_data = []
    with open(filename) as fh:
        for row in csv.DictReader(fh, fieldnames=("name", "sex", "count")):
            if row["sex"] == "F":
                female_data.append({"name": row["name"], "count": int(row["count"])})
            else:
                male_data.append({"name": row["name"], "count": int(row["count"])})
    return female_data, male_data


def get_count(row):
    return row["count"]


def most_popular(data):
    sorted_names = sorted(data, key=get_count, reverse=True)
    return sorted_names[0]


def rank(data, name):
    total = 0
    name_count = 0
    for counter, row in enumerate(data):
        total += row["count"]
        if row["name"] == name:
            name_count = row["count"]
    return (name_count / total) * 100


def popularity(name, sex):
    series = []
    for year in range(1880, 2019):
        female, male = get_year(year)
        if sex == "F":
            series.append({"year": year, "rank": rank(female, name)})
        else:
            series.append({"year": year, "rank": rank(male, name)})
    return series


def chart_popularity(name, sex):
    x = []
    y = []
    series = popularity(name, sex)
    for row in series:
        x.append(row["year"])
        y.append(row["rank"])
    seaborn.relplot(x=x, y=y, kind="line")
