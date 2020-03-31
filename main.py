import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = pd.read_csv('cardio_train.csv', sep=';', nrows=100)



# Show the results of a linear regression within each dataset
sns.lmplot(x="ap_hi", y="cardio", data=df,
           ci=None, palette="muted", hue="gluc",
           scatter_kws={"s": 50, "alpha": 1})

#sns.lineplot(x="age", y="ap_hi",
#             data=df)

#sns.relplot(x="trestbps", y="age", hue="num", style="num",
#            data=df)

#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
plt.show()