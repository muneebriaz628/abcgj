#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv('happyscore_income.csv')
print(df.head())
df.hist()
plt.show()


# In[ ]:




