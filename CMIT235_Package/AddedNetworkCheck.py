# Name: Nate Lanfranca
# Date: 2/29/2024
# Assignment: Week 7 - Advanced Functions
# Description: Using iterators and generators in a separate class
from scapy.layers.inet import TCP

import CMIT235_Package.NewNetworkCheck as nnc

class AddedNetworkCheck(nnc.NewNetworkClass):

    def __init__(self):
        super().__init__()

    def getPingCount(self, pcapFile):
        count = 0
        # Iterate through the pcap file
        for packet in pcapFile:
            if packet.haslayer(TCP):
                if packet[TCP].window == 4095:
                    count += 1
        return count

    def callGrandparent(self, arrayParam):
        gpMax = super().getMax(arrayParam)
        print(gpMax)
