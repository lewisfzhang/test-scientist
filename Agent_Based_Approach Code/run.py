# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:05:55 2018

@author: zstemple
"""

# run.py
# import os
# os.chdir("C:/Users/zstemple/Documents/GitHub/Scientist-Simulation/Agent_Based_Approach Code")
from model import *
# import sys

# orig_stdout = sys.stdout
# f = open("output.txt", "w")
# sys.stdout = f

test_model = ScientistModel(N = 2, ideas_per_time = 1, time_periods = 3)
# NOTE: To iterate once through a model, the number of steps should be time
# periods + 2
for i in range(5):   
    test_model.step()

scien_vars_time = test_model.datacollector.get_agent_vars_dataframe()
model_vars_time = test_model.datacollector.get_model_vars_dataframe()
print(scien_vars_time.to_string())
print(model_vars_time.to_string())
print(test_model.total_effort)
#
# sys.stdout = orig_stdout
# f.close()