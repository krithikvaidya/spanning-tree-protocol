from .classes import Message, Bridge


# Print the adjacent LANs for each bridge
def print_bridge_network(bridge_network):

    for bridge in bridge_network:

        print(bridge.id, end = ': ')

        for adj_LAN in bridge.adj_LANs:
            print(adj_LAN, end = ' ')
        print()


# Print adjacent bridges for each LAN

def SendMessage(message, bridge_network, LAN_network):
	messages = []  # stored in order of destination
	root = message.root
	dist = message.dist
	source = message.source

	bridge = bridge_network[source.id - 1]

	for adj_LAN in bridge.adj_LANs:
		for LAN in LAN_network:
			if adj_LAN == LAN.id:
				for LAN_adj_bridge in LAN.adj_bridges:
					if LAN_adj_bridge != source.id:
						messages += Message(root, dist, source, LAN_adj_bridge, LAN.id)
					
	return messages


def UpdateConfig(message, bridge_network):  # lists are mutable
	root = message.root
	dist = message.dist  
	source = message.source  # might need to do imports for the datatype
	dest = message.dest
	LAN = message.LAN

	return_message = Message(root = -1, dist = -1, source = None, dest = -1, LAN = None)  # might cause error because not passing params to constructor

	bridge = bridge_network[dest - 1]

	if (root < bridge.root) or ((root == bridge.root) and (dist + 1 < bridge.root_distance)) or ((root == bridge.root) and (dist + 1 == bridge.root_distance) and (source.id < bridge.root_port[1])):
		# hoping that custom class objects are mutable.

		return_message.root = root
		return_message.dist = dist + 1
		return_message.source = bridge
		bridge.root = root
		bridge.root_port = (LAN, source.id)
		bridge.root_distance = dist + 1
		
	else:
		return_message.root = -1
		return_message.dist = dist + 1
		return_message.source = bridge

	return return_message