import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = pd.read_csv('heart.csv')

# Show the results of a linear regression within each dataset
sns.lmplot(x="age", y="target", data=df,
           ci=None, palette="muted",
           scatter_kws={"s": 50, "alpha": 1})

#sns.relplot(x="trestbps", y="age", hue="target", style="target",
#            data=df)

plt.show()