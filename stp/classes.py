class LAN:

    """
    id = '\0';
	DP = -1;
    """

    def __init__(self, lan_id, desig_port, adj_bridges, hosts_in_lan):
        self.lan_id = lan_id
        self.desig_port = desig_port
        self.adj_bridges = adj_bridges
        self.hosts_in_lan = hosts_in_lan


class Forwarding_Table:
    def __init__(self, host_id, lan_forwarding_port):
        self.host_id = host_id
        self.lan_forwarding_port = lan_forwarding_port


class Bridge:

    """ 
    id = -1;
    root = id;
    RP = make_pair('\0',-1);
    root_distance = -1;
    """

    def __init__(self, bridge_id, root_id, root_distance, adj_LANs, forwarding_table, root_port):
        self.bridge_id = bridge_id
        self.root_id = root_id
        self.root_distance = root_distance
        self.adj_LANs = adj_LANs
        self.forwarding_table = forwarding_table
        self.root_port = root_port


class Message:

    """
    root = -1;
    dist = -1;
    destination = -1;
    lan = '\0';
    """
    def __init__(self, root, dist, source, dest, LAN):
        self.root = root
        self.dist = dist
        self.source = source
        self.dest = dest
        self.LAN = LAN


    def __gt__(self, other): 
        if(self.dest > other.dest): 
            return True
        else: 
            return False

# class Traces
# data packet class for data packet sending simulation