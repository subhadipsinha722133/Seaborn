import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("tips")
print(var)

sns.countplot(x="sex", data=var)
plt.show()
