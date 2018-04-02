
# coding: utf-8

# In[1]:


#計算機程式(package)/source/calculator.py


# In[2]:


def Calculator(arg1,arg2,operator):
    if operator == '+':
        print (int(arg1) + int(arg2))
    if operator == '-':
        print (int(arg1) - int(arg2))
    if operator == '*':
        print (int(arg1) * int(arg2))
    if operator == '/':
        print (int(arg1) / int(arg2))

