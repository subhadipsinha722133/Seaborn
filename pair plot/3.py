import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

v = sns.load_dataset("tips")
print(v)


sns.pairplot(v, vars=["total_bill", "tip"], hue="sex", hue_order=["Female", "Male"])
plt.show()
