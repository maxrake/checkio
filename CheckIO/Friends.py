
class Friends:
    """The class "Friends" should contains names and the connections between them.
    Names are represented as strings and are case sensitive.
    Connections are undirected, so if "sophia" is connected with "nikola",
    then it's also correct in reverse.
    """

    def __init__(self, connections):
        """Returns a new Friends instance.
        "connections" is an iterable of sets with two elements in each.
        Each connection contains two names as strings. Connections can
        be repeated in the initial data, but inside it's stored once.
        Each connection has only two states - existing or not.
        """
        
        # create an empty dictionary
        self._conndb = {}

        for conn in connections:
            conn_list = list(conn)
            friend1 = conn_list[0]
            friend2 = conn_list[1]
            
            if friend1 not in self._conndb:
                self._conndb[friend1] = set()
                self._conndb[friend1].add(friend2)
            else:
                self._conndb[friend1].add(friend2)
            if friend2 not in self._conndb:
                self._conndb[friend2] = set()
                self._conndb[friend2].add(friend1)
            else:
                self._conndb[friend2].add(friend1)


    def add(self, connection):
        """Add a connection in the instance.
        "connection" is a set of two names (strings).
        Returns True if this connection is new.
        Returns False if this connection exists already.
        """
        
        conn_list = list(connection)
        friend1 = conn_list[0]
        friend2 = conn_list[1]

        # check for existing connection
        if friend1 in self._conndb and friend2 in self._conndb[friend1]:
            return False
        
        # doesn't exist already...add the connection
        if friend1 not in self._conndb:
            self._conndb[friend1] = set()
            self._conndb[friend1].add(friend2)
        else:
            self._conndb[friend1].add(friend2)
        if friend2 not in self._conndb:
            self._conndb[friend2] = set()
            self._conndb[friend2].add(friend1)
        else:
            self._conndb[friend2].add(friend1)

        return True


    def remove(self, connection):
        """Remove a connection from the instance.
        "connection" is a set of two names (strings).
        Returns True if this connection exists.
        Returns False if this connection is not in the instance.
        """

        conn_list = list(connection)
        friend1 = conn_list[0]
        friend2 = conn_list[1]

        # check for non-existing connection...nothing to remove
        if friend1 not in self._conndb or friend2 not in self._conndb:
            return False
        
        # connection exists...remove it
        self._conndb[friend1].remove(friend2)
        self._conndb[friend2].remove(friend1)
        
        # remove keys from the conndb dict if they contain empty sets
        if not self._conndb[friend1]:
            del self._conndb[friend1]
        if not self._conndb[friend2]:
            del self._conndb[friend2]

        return True


    def names(self):
        """Returns a set of names.
        The set contains only names which are connected with somebody.
        """

        return {name for name in self._conndb}


    def connected(self, name):
        """Returns a set of names which is connected with the given "name".
        If "name" does not exist in the instance, then return an empty set.
        """

        if name not in self._conndb:
            return set()
        else:
            return self._conndb[name]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    print(letter_friends.names())
    assert letter_friends.connected("d") == set(), "Non connected name"
    print(letter_friends.connected("d"))
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    print(letter_friends.connected("a"))