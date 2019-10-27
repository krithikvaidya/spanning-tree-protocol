""" void print_bridge_network(vector<bridge> network)
{
	for(int i=0; i<network.size();i++)
	{
		cout<<network[i].id<<endl;
		for(int j=0; j<network[i].adj_lans.size();j++)
			cout<<network[i].adj_lans[j]<<" ";
		cout<<endl;
	}
} """

# Print the adjacent LANs for each bridge
def print_bridge_network(bridge_network):

    for bridge in bridge_network:

        print(bridge.id, end = ': ')

        for adj_LAN in bridge.adj_LANs:
            print(adj_LAN, end = ' ')
        print()


""" void print_lan_network(vector<lan> network)
{
	for(int i=0; i<network.size();i++)
	{
		cout<<network[i].id<<endl;
		for(int j=0; j<network[i].adj_bridges.size();j++)
			cout<<network[i].adj_bridges[j]<<" ";
		cout<<endl;
		cout<<network[i].DP<<endl;
	}
}




typedef set<message,messageComparer> messageSet;

messageSet SendMessage(message m,vector<bridge> bridge_network, vector<lan> lan_network)
{
	messageSet messages;
	int root = m.root;
	int d = m.dist;
	bridge source = m.source;
	for(int i=0; i<bridge_network.size();i++)
		if(source.id == bridge_network[i].id)
			for(int j=0; j<bridge_network[i].adj_lans.size(); j++)
				for(int k=0; k<lan_network.size(); k++)
					if(bridge_network[i].adj_lans[j] == lan_network[k].id)
						for(int p=0; p<lan_network[k].adj_bridges.size();p++)
							if(lan_network[k].adj_bridges[p] != source.id)
							{
								message ms;
								ms.root = root;
								ms.dist = d;
								ms.source = source;
								ms.destination = lan_network[k].adj_bridges[p];
								ms.lan = lan_network[k].id;
								messages.insert(ms);
							}
	return messages;
}

message UpdateConfig(message m,vector<bridge>& bridge_network)
{
	int root = m.root;
	int d = m.dist;
	bridge source = m.source;
	int destination = m.destination;
	char lan = m.lan;

	message return_message;

	for(int i=0; i<bridge_network.size();i++)
	{
		if(destination == bridge_network[i].id)
		{
			bridge b = bridge_network[i];
			if(root < b.root)
			{
				return_message.root = root;
				return_message.dist = d+1;
				return_message.source=bridge_network[i];
				bridge_network[i].root = root;
				bridge_network[i].RP = make_pair(lan,source.id);
				bridge_network[i].root_distance = d+1;
			}
			else if(root == b.root && d+1 < bridge_network[i].root_distance)
			{
				return_message.root = root;
				return_message.dist = d+1;
				return_message.source=bridge_network[i];
				bridge_network[i].root = root;
				bridge_network[i].RP = make_pair(lan,source.id);
				bridge_network[i].root_distance = d+1;
			}
			else if (root == b.root && d+1 == bridge_network[i].root_distance && source.id<bridge_network[i].RP.second)
			{
				return_message.root = root;
				return_message.dist = d+1;
				return_message.source=bridge_network[i];
				bridge_network[i].root = root;				
				bridge_network[i].RP = make_pair(lan,source.id);
				bridge_network[i].root_distance = d+1;
			}
			else
			{
				return_message.root = -1;
				return_message.dist = d+1;
				return_message.source=bridge_network[i];
			}
		}
	}

	return return_message;
}

lan lookIntoTable(vector<ftable> forwarding_table, int d)
{
	lan l;
	l.id='\0';
	for(int i=0; i<forwarding_table.size();i++)
	{
		ftable f = forwarding_table[i];
		if(f.host == d) l = f.fport;
	}
	return l;
} """