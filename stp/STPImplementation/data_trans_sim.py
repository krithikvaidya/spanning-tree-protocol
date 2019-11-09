from ..classes import Message
from ..helpers import SendMessage, UpdateConfig, print_bridge_network, print_LAN_network

def update_LAN_network(bridge_network, LAN_network):

	for LAN in LAN_network:  # does it make copies of the list elements??

		c = LAN.lan_id
		l = []

		for bridge in bridge_network:

			for adj_LAN in bridge.adj_LANs:
			
				if adj_LAN == c:

					 l.append(bridge.bridge_id)

		LAN.adj_bridges = l
	
	print('\nFinal bridge network: \n')
	
	print_LAN_network(LAN_network)

	print()
	