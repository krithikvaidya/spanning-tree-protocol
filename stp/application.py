from .STPImplementation.create_topology import create_topo
from .stp_algo import implement_protocol, print_bridge_root_ports, print_port_statuses

def run():
    bridge_network = []
    LAN_network = []

    create_topo(bridge_network, LAN_network)
    
    implement_protocol(bridge_network, LAN_network)

    print_bridge_root_ports(bridge_network)
    print_port_statuses(bridge_network, LAN_network)

run()



    