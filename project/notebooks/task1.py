#!/usr/bin/env python
# coding: utf-8

# # Task 1: Terminal, VS Code and Jupyter
# ## Introduction 
# This notebook demonstrates Python performance using %timeit.

# In[1]:


numbers = list(range(1000))

#list comprehension
get_ipython().run_line_magic('timeit', '[x * 2 for x in numbers]')

#for loop
def multiply_using_loop(numbers):
    result = []
    for x in numbers:
        result.append(x*2)
    return result
get_ipython().run_line_magic('timeit', 'multiply_using_loop(numbers)')


# ## Performance Comparison
# 
# - List comprehension took 31.7 microseconds.
# - For loop took 37.1 microseconds.
# - List comprehension was faster in this test.
# - %timeit measures the execution time of Python code.

# ## When to Use Jupyter Notebook and Python File
# 1. Juoyter Notebook is useful for data analysis and experimantation.
# 2. It allows us to execute code cell by cell.
# 3. Python (.py) files are useful for developing and automation.
# 4. Python files are suitable for reusable and production-level code.

# 
