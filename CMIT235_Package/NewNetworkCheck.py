# Name: Nate Lanfranca
# Date: 2/16/2024
# Assignment: Week 7 - Advanced Functions
# Description: Overriding the NetworkCheck class

# Import the NetworkCheck class
import CMIT235_Package.NetworkCheck as nc
import numpy as np

class NewNetworkClass(nc.NetworkCheck):
    def __init__(self):
        super().__init__()

    def getDescriptingInfo(self, sublists):
        tempArray = np.array(sublists)
        newDict = {'NumberOfDimensions': [], 'Shape': [], 'Mean': [], 'Median': [], 'StandardDeviation': []}
        for sublist in tempArray:
            newDict['NumberOfDimensions'].append(np.ndim(sublist))
            newDict['Shape'].append(np.shape(sublist))
            newDict['Mean'].append(np.mean(sublist))
            newDict['Median'].append(np.median(sublist))
            newDict['StandardDeviation'].append(np.std(sublist))
        return newDict

    def callSuper(self, arrayParam):
        supMin = super().getMin(arrayParam)
        print(supMin)
