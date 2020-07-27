# -*- coding: utf-8 -*-


import math
import numpy
import seaborn as sns
from NormalDistribution.Distributions import Distribution

class Normal(Distribution):
    def __init__(self, mean, std):
        Distribution.__init__(self, mean, std)
        
    def calculate_mean(self):
        ## This function takes in the data list and return the mean of the data
        
        mean_list = sum(self.data)/len(self.data)
        self.mean = mean_list
        
        return self.mean
    
    def calculate_std(self, sample=True):
        ## This function takes in the data list and return the standard deviation of the data
        
        if sample:
            n = len(self.data)-1
        if not sample:
            n = len(self.data)
        sum_data = 0
        
        for data_point in self.data:
            sum_data += (data_point - (self.calculate_mean()))**2
            
        sum_data = sum_data/n
        sigma = math.sqrt(sum_data)
        self.stdev = sigma
        
        return self.stdev
        
    def distribution_plot(self):
        ## This function plot the normal distribution plot for the data
        
        ax = sns.distplot(self.data)
        ax.set(xlabel="data_list", ylabel="data_count")
        ax.set_title("Normal Distribution")
        
    def normal_distribution(self, x):
        ## This function takes in a data point and return the Gussian distribution value for it
        
        return ((1/math.sqrt(2*math.pi*(self.stdev **2))) * math.exp(-0.5*((x-self.mean) / self.stdev)**2))
    
    def add_distribution(self, other):
        ## Other: Normal instance
        ## This function combine the mean and standard deviation for two Normal(Gussian) distributions
       
        result = Normal()
        
        result.mean = self.mean + other.mean
        result.std = math.sqrt(self.stdev**2 + other.stdev**2)
        
        return result
        
    def total_distribution(self):
        ## This function return the mean and the standard deviation of the combined Gussian distribution
        
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
        
