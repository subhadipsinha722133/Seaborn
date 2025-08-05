import matplotlib.pyplot as plt
import seaborn as sns


var = sns.load_dataset("tips")
print(var)

sns.stripplot(x="day", y="total_bill", data=var, hue="sex")
plt.show()
