# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %%
plt.close('all')
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2020', periods=1000))
ts = ts.cumsum()
# %%
ts.plot()
# %%
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
# %%
df.plot()
# %%
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B')


# %%
