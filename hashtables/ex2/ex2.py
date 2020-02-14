#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    count = 0
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
        
    for i in tickets:
        if i.source == 'NONE':
            destination = i.destination
            while destination:
                route[count] = destination
                newdes = destination
                destination = hash_table_retrieve(hashtable, newdes)
                count += 1
                if destination == "NONE":
                    route[count] = destination
                    break  

    return route


