# show distribution of variables in the dataset fairfield.data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df = pd.read_csv("data.csv", encoding="ISO-8859-1", low_memory=False)


# set column names
df.columns

# show distribution of variables
df.hist(figsize=(10, 10))
plt.show()

# show correlation matrix
corr = df.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
plt.show()


# show distribution of variables in the dataset fairfield.data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df = pd.read_csv("data.csv", encoding="ISO-8859-1", low_memory=False)

variables = df.columns.delete(2)

mercuery = df["Mercury"].values

fig = plt.figure(figsize=(10, 10))
plt.title("Distribution of Mercury by different variables")


for var in variables:
    fig.add_subplot(3, 4, variables.get_loc(var) + 1)
    plt.scatter(df[var], mercuery)
    plt.title("Mercury vs. {}".format(var))
    plt.xlabel(var)
    plt.ylabel("Mercury")
    plt.grid()
    plt.show()

plt.show()
