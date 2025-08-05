import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

v = sns.load_dataset("tips")
print(v)

sns.pairplot(v)
plt.show()
