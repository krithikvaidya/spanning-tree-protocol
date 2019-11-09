from ..classes import Message, LANN, Data_Packet, Forwarding_Table
from ..helpers import SendMessage, UpdateConfig, print_bridge_network, print_LAN_network
from ..helpers import lookIntoTable

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


def transfer_simulation(bridge_network, LAN_network):

	# First accept all hosts connected to the 
	# given LAN as input

	print('\nEnter the hosts present in each LAN: \n')

	for LAN in LAN_network:

		host_list = input(f'Enter the hosts connected to LAN {LAN.lan_id}: ').split()

		for host in host_list:
			LAN.hosts_in_lan.append(host)

	
	# Now take input of the endpoints for the data transfer simulation

	print('\nEnter the data transfer endpoints: ')
	source = input('1. Source: ')
	dest = input('2. Dest: ')

	host_LAN = None

	for LAN in LAN_network:
		for host in LAN.hosts_in_lan:
			if host == source:
				host_LAN = LAN
				break

	
	sent = []
	recvd = []

	for bridge in host_LAN.adj_bridges:
		data = Data_Packet(source, dest, host_LAN.lan_id, bridge)
		recvd.append(data)

	flag = 1

	while len(sent) > 0 or flag == 1:

		# first process sent packets
		while len(sent) > 0:
			data = sent.pop(0)

			if data.bridge > 0:
				recvd.append(data)

			else:
				ds = -1 * data.bridge
				la = data.prev
				l = None

				for LAN in LAN_network:
					if LAN.lan_id == la:
						l = LAN

				for bridge in l.adj_bridges:
					if ds != bridge:
						data.bridge = bridge
						recvd.append(data)

		# then process received packets
		
		while len(recvd) > 0:

			data = recvd.pop(0)

			for bridge in bridge_network:
				if data.bridge == bridge.bridge_id:
					lookin = lookIntoTable(bridge.forwarding_table, dest)
					if lookin:
						f = 0
						for host_in_LAN in lookin.hosts_in_lan:
							if host_in_LAN == data.dest:
								f = 1

								for adj_bridge in lookin.adj_bridges:

									for bridge2 in bridge_network:
										
										if bridge.id != bridge2.id and bridge2.id == adj_bridge and (lookIntoTable(bridge2.forwarding_table, source).id is None):
											e = Forwarding_Table(source, lookin)
											bridge2.forwarding_table.append(e)

											# trace stuff


						if f == 0 and data.prev != lookin.lan_id:

							for adj_bridge in lookin.adj_bridges:

								data_to_send = Data_Packet(data.source, data.dest, lookin.lan_id, adj_bridge)
								if adj_bridge != bridge.id:
									sent.append(data_to_send)

						if lookIntoTable(bridge.forwarding_table, source).lan_id is None:
							fport = None
							for LAN in LAN_network:
								if LAN.id == data.prev:
									fport = LAN

							bridge.forwarding_table.append(Forwarding_Table(source, fport))

					else:
						fport = None
						for LAN in LAN_network:
							if LAN.lan_id == data.prev:
								fport = LAN

						bridge.forwarding_table.append(Forwarding_Table(source, fport))

						for adj_LAN in bridge.adj_LANs:
							data_to_send = Data_Packet(data.source, data.dest, adj_LAN, -1 * bridge.bridge_id)

							if data.prev != adj_LAN:
								sent.append(data_to_send)
			
		flag = 0			

	for bridge in bridge_network:
		
		print(f'B{bridge.bridge_id}: ')
		print('HOST ID | FORWARDING PORT')
		
		for ftable_entry in bridge.forwarding_table:

			print(f'H{ftable_entry.host} | {ftable_entry.fport.lan_id}')
				
			
		print()