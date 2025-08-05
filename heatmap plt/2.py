import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# var = np.linspace(1, 10, 20).reshape(4, 5)
# print(var)
data = sns.load_dataset("anagrams")
print(data)
x = data.drop(columns=["attnr"], axis=1)
print(x)

sns.heatmap(x)
plt.show()
