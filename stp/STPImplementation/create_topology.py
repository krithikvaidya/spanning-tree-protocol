import sys  # for command-line arguments

from ..classes import LANN, Bridge
from ..helpers import print_bridge_network, print_LAN_network

def create_topo(bridge_network, LAN_network):  
    """Creates the network topology according to user input"""

    if len(sys.argv) != 2:
        print('Usage: python network.py <number of bridges>')
        sys.exit(1)

    bridge_count = int(sys.argv[1])

    if bridge_count <= 0:
        print("Please enter a valid number of bridges!\n")
        sys.exit(1)

    LAN_set = []
    
    print('\nEnter the adjacent LANs for each bridge: ')

    """
    The loop below takes in the list of LANs each bridge
    is connected to as input, sorts it and creates a new
    bridge object that is added to our bridge_network. It
    also creates the set of unique LANs in our network,
    LAN_set.
    """

    # TODO: error checking for duplicate LANs

    for i in range(bridge_count): 

        LAN_list = []

        print(f"B{i + 1}:", end = " ")
        inp = input().split()

        for LAN in inp:
        	LAN_list.append(int(LAN))

        LAN_list.sort()

        # add unique LANs to LAN_set, if not
        # already existing
        for bridge_LAN in LAN_list:
            flag = 1
            for LANs in LAN_set:
                if LANs == bridge_LAN:
                    flag = 0

            if flag == 1:
                LAN_set.append(bridge_LAN)

        bridge_network.append(Bridge(i, i, 0, LAN_list, [], [None, -1]))
        
    # Creation of bridge_network and LAN_set done.

    LAN_set.sort()

    """
    now we will construct the LAN_network consisting of the
    list of LANs and the bridges to which each one of them is
    connected to.
    """  

    for LAN_id in LAN_set:
        lan = LANN(lan_id=LAN_id, desig_port=-1, adj_bridges=[], hosts_in_lan=0)
        for bridge in bridge_network:
            for bridge_LAN in bridge.adj_LANs:
                if bridge_LAN == LAN_id:
                    lan.adj_bridges.append(bridge.bridge_id)

        # print(lan.adj_bridges) if you want to see the adjacent bridges for each LAN
        LAN_network.append(lan)

    # creation of LAN_network done.




