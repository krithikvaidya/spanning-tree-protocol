from ..classes import Message
from ..helpers import SendMessage, UpdateConfig, print_bridge_network, print_LAN_network
import math

def implement_protocol(bridge_network, LAN_network):
	""" 
	Implements the Spanning Tree Protocol algorithm after
	the construction of the network topology.
	"""

	spawned = []  # stores messages that have been sent in each iteration
	received = []  # stores received messages in each iteration

	curr_time = 0

	# initial message spawned by each bridge.
	for bridge in bridge_network:
		msg = Message(bridge.bridge_id, 0, bridge, -1, None)
		spawned.append(msg)

	# first iteration.
	"""
	Pops each message in the spawned list(could've been implemented
	as a queue) and simulates the sending using the SendMessage() function
	(defined in helpers.py).
	"""
	while spawned:
		m = spawned.pop(0) 
		received_by_set = SendMessage(m, bridge_network, LAN_network)

		for message in received_by_set:
			received.append(message)

		curr_time += 1

	# subsequent iterations
	while True:

		# clear out spawned
		spawned = []

		while received:

			# TODO: add received trace.

			m = received.pop(0)
			to_be_published = UpdateConfig(m, bridge_network)

			if to_be_published.root != -1:
				spawned.append(to_be_published)

		if not spawned:
			break

		while spawned:
			m = spawned.pop(0)

			received_by_set = SendMessage(m, bridge_network, LAN_network)

			for message in received_by_set:
				received.append(message)

		curr_time += 1

def print_bridge_root_ports(bridge_network):
	print()
	print('Root ports for bridges: ')
	print()

	for bridge in bridge_network:
		print(f'{bridge.bridge_id} {bridge.root_port[0]}')
	
	print()

def print_port_statuses(bridge_network, LAN_network):

	for i in range(len(LAN_network)):
		temp = math.inf
		for adj_bridge in LAN_network[i].adj_bridges:
			if adj_bridge < temp:
				temp = adj_bridge

		LAN_network[i].desig_port = temp

	print()
	# print("Designated ports for lans: ")
	print()
	# print_LAN_network(LAN_network)
	print()

	for bridge in bridge_network:
		
		# print(f'B{bridge.bridge_id}:')
		for j in range(len(bridge.adj_LANs)):

			try:
				LAN = bridge.adj_LANs[j]
			except IndexError:
				break
				
			flag = 0
			c = LAN
			print(f' {c}-', end = '')

			if c == bridge.root_port[0]:
				print('RP', end = '')
				flag = 1

			for LAN in LAN_network:
				if (c == LAN.lan_id) and (bridge.bridge_id == LAN.desig_port) and (flag == 0):
					print('DP', end = '')
					flag = 1
					break

			if flag == 0:
				print('NP', end='')
				
				list(filter((c).__ne__, bridge.adj_LANs))
				
				j -= 1

		print()