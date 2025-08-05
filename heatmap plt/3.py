import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

d = sns.load_dataset("anagrams")
x = d.drop(columns=["attnr"], axis=1).head(10)
print(x)

sns.heatmap(x)
plt.show()
