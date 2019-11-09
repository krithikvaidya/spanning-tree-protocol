from .classes import Message, Bridge


# Print the adjacent LANs for each bridge
def print_bridge_network(bridge_network):

    for bridge in bridge_network:

        print(bridge.bridge_id, end = ': ')

        for adj_LAN in bridge.adj_LANs:
            print(adj_LAN, end = ' ')
        print()


# Print adjacent bridges for each LAN
def print_LAN_network(LAN_network):

	for LAN in LAN_network:

		print(f'\nAdjacent Bridges for LAN {LAN.lan_id}: ', end = '')

		for adj_bridge in LAN.adj_bridges:
			print(adj_bridge + 1, end = ' ')
		
		print(f'\nDesignated port for LAN {LAN.lan_id}: {LAN.desig_port + 1}')
	


def SendMessage(message, bridge_network, LAN_network):
	"""
	After a bridge spawns a message, it reaches other bridges.
	This function returns the list of messages received by other
	bridges, ordered by destination.
	"""

	messages = []  # stored in order of destination

	root = message.root
	dist = message.dist
	source = message.source

	bridge = bridge_network[source.bridge_id]

	for adj_LAN in bridge.adj_LANs:
		for LAN in LAN_network:
			if adj_LAN == LAN.lan_id:
				for LAN_adj_bridge in LAN.adj_bridges:
					if LAN_adj_bridge != source.bridge_id:
						messages.append(Message(root, dist, source, LAN_adj_bridge, LAN.lan_id))
	
	messages.sort()
	return messages


def UpdateConfig(message, bridge_network):  # lists are mutable
	
	root = message.root
	dist = message.dist  
	source = message.source
	dest = message.dest
	LAN = message.LAN

	return_message = Message(root = -1, dist = -1, source = None, dest = -1, LAN = None)

	bridge = bridge_network[dest]

	if (root < bridge.root_id) or ((root == bridge.root_id) and (dist + 1 < bridge.root_distance)) or ((root == bridge.root_id) and (dist + 1 == bridge.root_distance) and (source.bridge_id < bridge.root_port[1])):
		# hoping that custom class objects are mutable.

		return_message.root = root
		return_message.dist = dist + 1
		return_message.source = bridge
		bridge.root_id = root
		bridge.root_port = (LAN, source.bridge_id)
		bridge.root_distance = dist + 1
		
	else:
		return_message.root = -1
		return_message.dist = dist + 1
		return_message.source = bridge

	return return_message

def lookIntoTable(fwding_table, dest):
	l = None
	
	for ftable in fwding_table:
		if ftable.host == dest:
			l = ftable.fport
	
	return l