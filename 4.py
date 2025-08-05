import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd


var = sns.load_dataset("penguins")
print(var)


sns.displot(var["bill_length_mm"])
plt.show()
