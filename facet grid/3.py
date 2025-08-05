import matplotlib.pyplot as plt
import seaborn as sns


var = sns.load_dataset("tips")
print(var)

f = sns.FacetGrid(var, col="sex", hue="day")
f.map(plt.scatter, "total_bill", "tip").add_legend()
plt.show()
