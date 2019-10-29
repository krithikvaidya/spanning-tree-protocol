from .classes import Message
from .helpers import SendMessage, UpdateConfig

def implement_protocol(bridge_network, LAN_network):
    spawned = []
    received = []

    curr_time = 0

    for bridge in bridge_network:
        msg = Message(bridge.id, 0, bridge, -1, None)
        spawned += msg

    # first iteration
    while spawned:
        m = spawned.pop(0)
        received_by_set = SendMessage(m, bridge_network, LAN_network)

        for message in received_by_set:
            received += message

        curr_time += 1

    # subsequent iterations
    while True:

        # clear out spawned
        spawned = []

        while received:

            # todo: add received trace.

            m = received.pop(0)
            to_be_published = UpdateConfig(m, bridge_network)

            if to_be_published.root != -1:
                spawned += to_be_published

        if not spawned:
            break

        while spawned:
            m = spawned.pop(0)

            received_by_set = SendMessage(m, bridge_network, LAN_network)

            for message in received_by_set:
                received += message

        curr_time += 1
			
