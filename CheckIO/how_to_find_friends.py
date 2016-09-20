def check_connection(network, first, second):
    # start with an empty list to hold the sets
    conns = []

    # create sets of connections from the network
    for conn in network:
        # convert the connection string to a set of connections, S
        S = set(conn.split("-"))

        # add this as a new set to conns if neither end
        # of the connection is already in the list of sets
        if all([x.isdisjoint(S) for x in conns]):
            conns.append(S)
        # update all sets in the connections list with new connections
        for conn_set in conns:
            if not conn_set.isdisjoint(S):
                conn_set |= S

    # condense the list of sets into as few sets as possible
    # by updating any that overlap
    for S1 in conns:
        for S2 in conns:
            if not S1.isdisjoint(S2):
                S1 |= S2

    # check if the drones are related
    for conn_set in conns:
        # is the set of the first and second drone a subset
        # of any connection set in the list of connections?
        if set([first, second]) <= conn_set:
            # if so, we found a connection and can return
            return True
    
    # if we made it this far, then the drones are not connected
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman","mr99-robin",
         "dr101-out00","out00-nwing",),
         "dr101","mr99") == True, "Extra test #3"