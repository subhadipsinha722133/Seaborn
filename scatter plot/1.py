import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("penguins").head(10)
print(var)

# sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", data=var)
sns.scatterplot(x="bill_length_mm", y="bill_depth_mm", data=var, hue="sex")

plt.show()
