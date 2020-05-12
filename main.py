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
# plt.show()

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()