import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

v = sns.load_dataset("tips")
print(v)

sns.violinplot(x="day", y="total_bill", data=v)
plt.show()
