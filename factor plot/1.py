import matplotlib.pyplot as plt
import seaborn as sns


var = sns.load_dataset("tips")
print(var)

sns.factorplot(x="size", y="tip", data=var)
plt.show()
