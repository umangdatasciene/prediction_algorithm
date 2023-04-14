import pandas as pd
import seaborn as sns
from scipy.stats import f_oneway
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")


null_hypothesis = "The mean petal length is equal across all three species of iris (setosa, versicolor, and virginica)."
alt_hypothesis = "The mean petal length differs across at least one of the three species of iris."


setosa = iris[iris["species"] == "setosa"]["petal_length"].fillna(0)
versicolor = iris[iris["species"] == "versicolor"]["petal_length"].fillna(0)
virginica = iris[iris["species"] == "virginica"]["petal_length"].fillna(0)


f_stat, p_value = f_oneway(setosa, versicolor, virginica)

# Print results
print("Null hypothesis:", null_hypothesis)
print("Alternative hypothesis:", alt_hypothesis)
print("F-value:", f_stat)
print("P-value:", p_value)


alpha = 0.05


if p_value < alpha:
    print("We reject the null hypothesis.")
else:
    print("We accept the null hypothesis.")

# Visualize results using a boxplot
sns.boxplot(x="species", y="petal_length", data=iris)
plt.title("Distribution of petal length by species")
plt.show()
