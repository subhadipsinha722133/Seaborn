import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

v = np.linspace(1, 10, 10).reshape(2, 5)
print(v)

sns.heatmap(v, vmin=0, vmax=10, cmap="PuOr", annot=True)
# sns.heatmap(v)
v.set(xlabel="python", ylabel="subhadip")
plt.show()
