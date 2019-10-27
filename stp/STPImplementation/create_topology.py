import sys
import os
from ..classes import LAN, Bridge

def create_topo():
    if len(sys.argv) != 2:
        print('Usage: python network.py <number of bridges>')
        sys.exit (1)

    bridge_count = int(sys.argv[1])

    if bridge_count <= 0:
        print("Please enter a valid number of bridges!\n")
        sys.exit(1)
    
    bridge_network = []
    LAN_set = set()

    print('\nEnter the adjacent LANs for each bridge: ')

    # todo: error checking for duplicate LANs

    for i in range(bridge_count):
        print('B' + (i + 1) + ': ', end = '')

        LAN_list = [int(LAN) for LAN in input().split()]
        LAN_list.sort()

        for bridge_LAN in LAN_list:
            LAN_set.add(bridge_LAN)

        # todo - improve constructor stuffs.

        bridge_network += Bridge(i, i, 0, LAN_list, [], -1)
        
    # Creation of bridge_network and LAN_set done.

    # now we will construct the LAN network consisting of the
    # list of LANs and the bridges to which each one of them is
    # connected to.

    LAN_network = []

    for LAN_id in LAN_set:
        lan = LAN(lan_id=LAN_id, desig_port=-1, adj_bridges=[], hosts_in_lan=0)
        for bridge in bridge_network:
            for bridge_LAN in bridge.adj_LANs:
                if bridge_LAN == LAN:
                    lan.adj_bridges += bridge.bridge_id

        LAN_network += lan

    # creation of LAN_network done.
    





