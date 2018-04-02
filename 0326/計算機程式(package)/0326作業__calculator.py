
# coding: utf-8

# # 作業4

# In[1]:


#計算機程式(package)/0326作業__calculator.py


# In[2]:


arg1 = input("請輸入第一個數字:")
arg2 = input("請輸入第二個數字:")
operator = input("請輸入運算子:")

from source import calculator
calculator.Calculator(arg1,arg2,operator)

