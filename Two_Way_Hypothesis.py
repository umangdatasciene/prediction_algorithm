import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


iris = sns.load_dataset("iris")


iris.fillna(0, inplace=True)


null_hypothesis = "There is no significant interaction between the species and the petal width in determining petal length."
alt_hypothesis = "There is a significant interaction between the species and the petal width in determining petal length."


model = ols('petal_length ~ species + petal_width + species:petal_width', data=iris).fit()


anova_table = anova_lm(model, typ=2)


print("Null hypothesis:", null_hypothesis)
print("Alternative hypothesis:", alt_hypothesis)
print(anova_table)


alpha = 0.05


if anova_table['PR(>F)'][2] < alpha:
    print("We reject the null hypothesis.")
else:
    print("We accept the null hypothesis.")
