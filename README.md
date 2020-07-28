This package is created for statistical analysis and for probability density function calculation. 
Statistical analysis involving calculation of mean and standard  deviation of a given data set.

The package has two classes

class Distribution: This contains two methods
    method(class attributes)
    method data_loader(file): This takes in a file in text format and append
    the data to a data list for calculations.
    
class Normal: This contains six methods
    methods calculate_mean(), calculate_std(), distribution_plot(),
    normal_distribution(x), add_distribution(other), total_distribution()
    
    calculate_mean() returns the mean of the data set.
    
    calculate_std() returns the standard deviation of the data set.
    
    distribution_plot() returns the histogram plot of the data set to visualize the distribution.
    
    normal_distribution() returns the probability density function value for a given
    point.
    
    to add two normal distributions together, add_distribution(other) where 
    other=Gussian returns the mean and standard deviation for the multiple 
    distribution
    
    total_distribution() returns the mean and the standard deviation for the 
    combined distribution
