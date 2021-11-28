import matplotlib.pyplot as plt
import pandas as pd


t = 'Этот мир прогнил'
list = list(t)
x = pd.DataFrame({'letters': list})
x['num'] = 1
x = x.groupby('letters').sum().sort_values('num', ascending=False) / len(x)

plt.bar(x.index, x.num, width=0.5)
plt.show()
