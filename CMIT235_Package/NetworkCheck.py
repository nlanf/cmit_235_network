# Name: Nate Lanfranca
# Date: 2/16/2024
# Assignment: Week 5 - Inheritance, Iterators, and Generators
# Description: Class to manage and reference functions for network administration

# Import the required packages
import numpy as np
import pandas as pd
from scapy.layers.inet import UDP
from scapy.layers.l2 import Ether
from multipledispatch import dispatch

# ------Week 3 Networking Class utilization------
class NetworkCheck:
    def __init__(self):
        self.__mac_count = 0
        self.__sport_count = 0
        self.__message1 = "Welcome to message 1"
        self._message2 = "Welcome to message 2"
        self.message3 = "Welcome to message 3"

    def getMessage1(self):
        return self.__message1

    def getMessage2(self):
        return self._message2

    def setSourcePortCount(self, pcapFile, portNumber):
        count = 0
        # Iterate through the pcap file
        for packet in pcapFile:
            if packet.haslayer(UDP):
                if packet.sport == portNumber:
                    count += 1
        self.__sport_count = count

    def getSourcePortCount(self):
        return self.__sport_count

    def setSourceMacCount(self, pcapFile, macAddress):
        count = 0
        # Iterate through the pcap file
        for packet in pcapFile:
            if packet[Ether].src == macAddress:
                count += 1
        self.__mac_count = count

    def getSourceMacCount(self):
        return self.__mac_count

    # ------Week 2 Networking Class utilization------

    def convertList2NpArray(self, listArg):
        return np.array(listArg)

    def getMax(self, newArray):
        return np.max(newArray)

    def getMin(self, newArray):
        return np.min(newArray)

    def getUniqueValues(self, newArray):
        return np.unique(newArray)

    def getDescriptingInfo(self, sublists):
        tempArray = np.array(sublists)
        newDict = {'NumberOfDimensions': [], 'Shape': [], 'LastItem': [], 'FirstColumn': [], 'SecondRow': []}
        for sublist in tempArray:
            newDict['NumberOfDimensions'].append(np.ndim(sublist))
            newDict['Shape'].append(np.shape(sublist))
            newDict['LastItem'].append(sublist[-1, -1])
            newDict['FirstColumn'].append(sublist[:, 0])
            newDict['SecondRow'].append(sublist[1])
        return newDict

    # -----Week 4 Overloading functions-----
    @dispatch(str, str)
    def checkCounts(self, csv_data, feature):
        data = pd.read_csv(csv_data)
        return data.value_counts(feature)

    @dispatch(str, str, str, str)
    def checkCounts(self, csv_data, feature1, feature2, feature3):
        data = pd.read_csv(csv_data)
        feature_dict = {}

        if feature1 is not None:
            feature_dict[feature1] = data.value_counts(feature1)
        if feature2 is not None:
            feature_dict[feature2] = data.value_counts(feature2)
        if feature3 is not None:
            feature_dict[feature3] = data.value_counts(feature3)

        return feature_dict
