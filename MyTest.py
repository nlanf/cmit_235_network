# Name: Nate Lanfranca
# Date: 2/16/2024
# Assignment: Week 5 - Inheritance, Iterators, and Generators
# Description: Explores the use and manipulation of python lists, numpy arrays, user-defined classes, scopes,
# overriding, overloading, and creating, importing, and referencing packages

# Import the numpy package as np
import numpy as np
import sys
import logging

# ----Logging Instantiation----

# Set the log file
logging.basicConfig(filename='log_file', filemode='w', level=logging.DEBUG)

# Create a logging object using hierarchy
logger = logging.getLogger(__name__)

# -----Logging Instantiation End----

# Import the rdpcap tool
from scapy.utils import rdpcap

# Import the CMIT235_Package.CMIT235_Tools as cm
import CMIT235_Package.CMIT235_Tools as cm

# Import the NetworkCheck class
import CMIT235_Package.NetworkCheck as nc

# Import the NewNetworkCheck class
import CMIT235_Package.NewNetworkCheck as nnc

import CMIT235_Package.AddedNetworkCheck as addednc

# Log the program start
logger.info('Program start')

# Combine the three sublists lists into one list and store the combined list into a new variable.
try:
    newList = [cm.mySubList1, cm.mySubList2, cm.mySubList3]
    if isinstance(newList, list):
        pass
    else:
        TypeError('The combined lists are not of the list type!')
        logger.error('The combined lists are not of the list type!')
        sys.exit(1)
except Exception as e:
    print(f'The system encountered an error: {e}')
    logger.error(f'Error on list conversion block: {e}')
    sys.exit(1)

# -----Week 1 work-----

# Print the combined list.
print('-----Week 1-----\n')
print('The combined list looks like this: ', newList)

# Convert the combined list to a nparray and store the array in a new variable.
newArray = np.array(newList)
print('The numpy array is: ', newArray)

# Using the newly created numpy array:
# Print the minimum value.
print('The minimum value is: ', + np.min(newArray))

# Print the maximum value.
print('The maximum value is: ', + np.max(newArray))

# Print the unique values.
print('The unique values are: ', np.unique(newArray))

# Create a loop which iterates each of the three sublists
for sublist in newArray:
    # Convert the sublist into an array (nparray).
    nparray = np.array(sublist)

    # Print the array.
    print(nparray)

    # Print the dimensions of the array.
    print("The dimensions of the array are:", np.ndim(nparray))

    # Print the shape of the array.
    print("The shape of the array is:", np.shape(nparray))

    # Print the last number, the first column, and the second row of the array.
    print("The last number of the array is:", nparray[-1, -1])
    print("The first column of the array is:", nparray[:, 0])
    print("The second row of the array is:", nparray[1])
    print()

# ------Week 2 - New version utilizing the NetworkCheck class------

print('------Week 2 - New version utilizing the NetworkCheck class------')

# Instantiating the class
newClass = nc.NetworkCheck()

# Log NetworkCheck Instantiation
logger.info('NetworkCheck object instantiated')

# Check the object type
if not isinstance(newClass, nc.NetworkCheck):
    TypeError(f'Expected type: {nc.NetworkCheck}, got: {type(newClass)}')
    logger.error(f'Expected type: {nc.NetworkCheck}, got: {type(newClass)}')
    sys.exit(1)

# Converting the lists to numpy array
newerArray = newClass.convertList2NpArray(newList)

# Check that the max and min values are within acceptable ranges
if newClass.getMax(newerArray) > 100:
    ValueError('The max value is over 100')

if newClass.getMin(newerArray) < -100:
    ValueError('The min value is below -100')

# Get and print the max of newerArray
print('The max value using the class object: ' + str(newClass.getMax(newerArray)))

# Get and print the min of newerArray
print('The min value using the class object: ' + str(newClass.getMin(newerArray)))

# Get and print the unique values of newerArray
print('The unique values using the class object: ' + str(newClass.getUniqueValues(newerArray)))

descriptiveInfo = newClass.getDescriptingInfo(newList)

# Check that the object is of dictionary type
if not isinstance(descriptiveInfo, dict):
    TypeError(f'Expected type: {type(dict)}, got: {type(descriptiveInfo)}')
    logger.error(f'Expected type: {type(dict)}, got: {type(descriptiveInfo)}')
    sys.exit(1)

# Iterating over the returned dictionary of items
for key, value in descriptiveInfo.items():
    print(f"{key}: {value}")

# ------Week 3 Networking Class utilization------
print("\n------Week 3 Networking Class utilization------\n")
networkClass = nc.NetworkCheck()

# -----Attempt to access message1 directly-----
print('Attempt to access message1 directly:')
try:
    print(f'Message one is: {networkClass.__message1}.\n')
except:
    print('Unable to access message1.\n')

# -----Attempt to access message1 using the getter method-----
print('Attempt to access message1 using the getter method:')
try:
    print(f'Message one is: {networkClass.getMessage1()}.\n')
except:
    print('Unable to access message1.\n')

# -----Attempt to access message 3 directly-----
print('Attempt to access message 3 directly:')
try:
    print(f'Message three is: {networkClass.message3}.\n')
except:
    print('Unable to access message3.\n')

# -----Attempt to print and justify all three messages------
print('Attempt to print and justify all three messages:')
try:
    print(f'{networkClass.getMessage1():>25}{networkClass.getMessage2():>25}{networkClass.message3:>25}\n')
except:
    print('Unable to access messages.\n')

# ------Instantiate the packet variable------
# First check that the file read was successful
try:
    packets = rdpcap(cm.pcap)
except Exception as e:
    print(f'There was an error reading the file: {e}')
    logger.error(f'Pcap file read error: {e}')
    sys.exit(1)

# ----------Sport----------
print('----------Sport----------')
try:
    # Set the sport value
    networkClass.setSourcePortCount(packets, cm.sport)
    # Get sport count
    # First check that the variable is the correct type
    if not isinstance(networkClass.getSourcePortCount(), int):
        TypeError(f'Expected type: {type(int)}, got: {type(networkClass.getSourcePortCount())}')
        logger.error(f'Expected type: {type(int)}, got: {type(networkClass.getSourcePortCount())}')
        sys.exit(1)
    else:
        print(f'The sport count is: {networkClass.getSourcePortCount()}\n')
except:
    print('Unable to get the sport count\n')

# ----------MAC------------
print('----------MAC------------')
try:
    # Set the mac value
    networkClass.setSourceMacCount(packets, cm.mac_address)
    # Get the mac count
    # First check that the variable is the correct type
    if not isinstance(networkClass.getSourceMacCount(), int):
        TypeError(f'Expected type: {type(int)}, got: {type(networkClass.getSourceMacCount())}')
        logger.error(f'Expected type: {type(int)}, got: {type(networkClass.getSourceMacCount())}')
        sys.exit(1)
    else:
        print(f'The MAC count is: {networkClass.getSourceMacCount()}\n')
except:
    print('Unable to get the MAC count\n')

# -----Week 4 Overriding and Overloading-----
print('-----Week 4 Overriding and Overloading-----\n')

# Instantiate the NewNetworkClass
newNetworkClass = nnc.NewNetworkClass()

# Log NewNetworkClass Instantiation
logger.info('NewNetworkClass Instantiated')

# Check the object type
if not isinstance(newNetworkClass, nnc.NewNetworkClass):
    TypeError(f'Expected type: {nnc.NewNetworkClass()}, got: {type(newNetworkClass)}')
    logger.error(f'Expected type: {nnc.NewNetworkClass()}, got: {type(newNetworkClass)}')
    sys.exit(1)

# Call the overriding descripting info
newDescriptiveInfo = newNetworkClass.getDescriptingInfo(newList)

# Iterating over the returned dictionary of items
print('----Print the dictionary of the new descriptive info----\n')
for key, value in newDescriptiveInfo.items():
    print(f"{key}: {value}")
print('\n')

# Using overriding function from NetworkCheck class
print('----Print the overriding function to return the count of protocol----\n')
chkCounts1 = newClass.checkCounts(cm.csv_data, cm.feature3)
print(f'{chkCounts1}\n')

# Iterating through the features using the overloading function
print('----Print the dictionary of all the passed features----\n')
chkCounts2 = newClass.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3)
for key, value in chkCounts2.items():
    print(f"{key}: {value}")


# -----Week 5 Inheritance, Iterators, and Generators-----
print('\n-----Week 5 Inheritance, Iterators, and Generators----\n')

# Create a new variable for the np array using the inherited function from NewNetworkClass
inheritedArray = newNetworkClass.convertList2NpArray(newList)

# Get and print the minimum value using the inherited function
print(f'The minimum value is: {newNetworkClass.getMin(inheritedArray)}\n')

# Get and print the maximum value using the inherited function
print(f'The maximum value is: {newNetworkClass.getMax(inheritedArray)}\n')

# Get and print the minimum value using the inherited function
print(f'The unique values are: {newNetworkClass.getUniqueValues(inheritedArray)}\n')

# Get the ping count from the AddedNetworkClass
addedNetworkCheck = addednc.AddedNetworkCheck()

# Log AddedNetworkClass Instantiation
logger.info('AddedNetworkClass Instantiated')

pingCount = addedNetworkCheck.getPingCount(packets)

# First check that the variable is the correct type
if not isinstance(pingCount, int):
    TypeError(f'Expected type: {type(int)}, got: {type(pingCount)}')
    logger.error(f'Expected type: {type(int)}, got: {type(pingCount)}')
    sys.exit(1)
else:
    print(f'The ping count is: {pingCount}\n')

# Set the MAC count
addedNetworkCheck.setSourceMacCount(packets,cm.mac_address)

# Get the MAC count
getMacCount = addedNetworkCheck.getSourceMacCount()
print(f'The MAC count is: {getMacCount}\n')

# Get and print the checkCounts function
getCheckCounts = addedNetworkCheck.checkCounts(cm.csv_data, cm.feature3)
for key, value in getCheckCounts.items():
    print(f'{key}: {value}')
