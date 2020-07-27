##  Defining the Gussian(Normal) distribution class

class Distribution:
    def __init__(self, mean=0, std=1):
        ## This function defined the attribute of a Gussian(Normal) distribution
        self.mean = mean
        self.stdev = std
        self.data = []
   
    def data_loader(self, file):
        ## This function takes in a file.txt and append it to the data to form a list
        
        with open(file) as data:
            datta = []
            data_line = data.readline()
            while data_line:
                datta.append(int(data_line))
                data_line = data.readline()
        data.close() 
        
        ## To update the attributes values to the mean of the data and the standard deviation of the data
        self.data = datta
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_std() 
        
