import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd


var = [1, 2, 3, 4, 5, 6, 7]
var_1 = [2, 3, 4, 1, 5, 6, 7]

y_1 = sns.load_dataset("tips")
print(y_1)


sns.lineplot(x="total_bill", y="tip", data=y_1, hue="sex")

plt.show()
