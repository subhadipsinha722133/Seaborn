import matplotlib.pyplot as plt
import seaborn as sns


var = sns.load_dataset("tips")
print(var)

f = sns.FacetGrid(
    var,
)
f.map(plt.scatter, "total_bill", "tip")
plt.show()
