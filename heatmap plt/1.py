import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

var = np.linspace(1, 10, 20).reshape(4, 5)
print(var)

sns.heatmap(var)
plt.show()
