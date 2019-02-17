#!/usr/bin/env python
# coding: utf-8

# # Signal Detection Theory

# In[1]:


import numpy
import matplotlib.pyplot as plt


# Initialize Global variables. 

# In[2]:


num_samples = 1000
noise_mean = 0
noise_sd = 1


# Function to return false alarm and hit rates. Takes in the number of samples, d-prime, signal's standard deviation and the criterion. Assumes standard normal for noise distribution.

# In[13]:


def sdt(num_samples, d_, signal_sd, lamb):
    fa_rate = (float)(numpy.sum(numpy.random.normal(noise_mean, noise_sd, num_samples)>lamb))/num_samples
    hit_rate = (float)(numpy.sum(numpy.random.normal(d_, signal_sd, num_samples)>lamb))/num_samples
    return (fa_rate, hit_rate)


# In[3]:


#def sdt(num_samples, d_, signal_sd, lamb):
#    fa_rate = (float)(numpy.sum(numpy.random.exponential(noise_mean, num_samples)>lamb))/num_samples
#    hit_rate = (float)(numpy.sum(numpy.random.exponential(d_, num_samples)>lamb))/num_samples
#    return (fa_rate, hit_rate)


# Plotting!. Calls the sdt function to obtain hit and false alarm rates. Runs through a range of criterion values to plot the ROC curve.

# In[4]:


def roc_plot(d_, signal_sd):
    for lamb in numpy.linspace(0, d_+signal_sd, 100):
        fa, h = sdt(num_samples, d_, signal_sd, lamb)
        plt.scatter(fa, h)
        plt.xlabel("False Alarm Rate")
        plt.ylabel("Hit Rate")


# In[8]:


roc_plot(0.3, 1)


# In[16]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# 
# ### interact takes in the function and arguments to that function passed as range to use them as slider-widgets
# 
# 

# In[18]:


#interact(roc_plot, d_=(-3, 4, 0.1), signal_sd = (0.5, 4, 0.1))

