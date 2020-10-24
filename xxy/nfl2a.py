#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gurobipy as gp
from gurobipy import GRB
from gurobipy import *
import pandas as pd
import numpy as np


# In[2]:


########################################
########### IMPORT DATA ################
########################################

#list of teams that are included in the analysis
Team_list={
0:"Atlanta Falcons",1:"Carolina Panthers",2:"Chicago Bears",3:"Detroit Lions",
4:"Green Bay Packers",5:"Minnesota Vikings",6:"New Orleans Saints",7:"New York Giants",
8:"Philadelpia Eagles",9:"Tampa Bay Buccaneers",10:"Washington Football Team",11:"Baltimore Ravens",
12:"Buffalo Bills",13:"Cincinnati Bengals",14:"Cleveland Browns",15:"Houston Texans",
16:"Indianapolis Colts",17:"Jacksonville Jaguars",18:"Miami Dolphins",19:"New England Patroits",
20:"New York Jets",21:"Pittsburgh Steelers",22:"Tennessee Titans",23:"Dalls Cowboys"}


W=set(list(range(0,12))) #set of weeks, total of 12 weeks
T=set(list(range(0,24))) #set of teams all, total of 24 teams
 #set of conference
D1=set(list(range(0,12)))  #set of AFC teams
D2=set(list(range(12,24))) #set of NFC teams

#read the distance file
E=pd.read_csv("distance.csv",index_col=0)


# In[3]:


########################################
########### MODEL ######################
########################################

# Create an empty model
m= gp.Model(name="NFL2")
# ADD DECISION VARIABLES HERE
x_var = m.addVars(T, T, W, vtype = GRB.BINARY, name = "X")


# In[4]:


week=13


# In[5]:


### #### CONSTRAINTS & OBJ FUNCTIONS #######
########################################

# ADD CONSTRAINTS
# add constraints that The season was limited to 12 weeks
m.addConstrs(sum(sum(x_var[i,j,k]+x_var[j,i,k] for k in W) for i in T) == 12 for j in T)
# add constraints that Each team would play once per week
m.addConstrs(sum(x_var[i,j,k]+x_var[j,i,k] for j in T) == 1 for i in T for k in W)
# add constraints that All 12 games that a team played would need to be against a different opponent
m.addConstrs(sum(x_var[i,j,k]+x_var[j,i,k]for k in W) <= 1 for i in T for j in T)
# add constraints that Each team would play at most six home games (i.e., on their home stadium)
m.addConstrs(sum(sum(x_var[i,j,k] for k in W) for j in T) <=6 for i in T)
# add constraints to avoid circumstances that i=i
m.addConstrs(x_var[i,i,k] == 0 for i in T for i in T for k in W)
# add constraints to let binary variables are bound between 0 and 1
m.addConstrs(x_var[i,j,k] <= 1 for i in T for j in T for k in W)
m.addConstrs(x_var[i,j,k] >= 0 for i in T for j in T for k in W)

# add gaming pattern constraints for 2a
m.addConstrs(sum(x_var[i,j,k]+x_var[i,j,k+1]+x_var[i,j,k+2] for j in T) <= 2 for i in T for k in range(week-3))
m.addConstrs(sum(x_var[i,j,k]+x_var[i,j,k+1]+x_var[i,j,k+2] for j in T) >= 1 for i in T for k in range(week-3))

# ADD OBJECTIVE FUNCTION
# Objective is to minimize the total travel distance of all teams
obj = sum(E.iloc[i,j]*x_var[i,j,k] for i in T for j in T for k in W)*2

#optimize the model
m.setObjective(obj, GRB.MINIMIZE)
m.optimize()


# In[6]:


########################################
########### PRINT RESULTS ##############
########################################

# ADD PRINTING
# Print optimal value of the objective function
print('\nValue of objective function: %g' % m.objVal)


# In[7]:


# Print optimal values for the decision variables
print('\nDecision variables:')
for v in m.getVars():
    if v.x !=0:
        print('%s = %g' % (v.varName, v.x))


# In[ ]:




