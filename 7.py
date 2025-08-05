import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

var = sns.load_dataset("penguins")
print(var)

# sns.barplot(x=var.island, y=var.bill_length_mm)
# sns.barplot(x="island", y="bill_length_mm", data=var)
# sns.barplot(x="island", y="bill_length_mm", data=var, hue="sex")
# m = ["sinha", "kumar", "subhadip"]
sns.barplot(x="bill_length_mm", y="bill_length_mm", data=var, hue="sex", orient="v")


plt.show()
