#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    spots = []
    indexes = []
   
    for i in range(len(weights)-1):
        hash_table_insert(ht, weights[i], i)
        
    # value is stored with the index of weights position

    for i in weights:
        if limit - i == i:
            return (1,0)
        if hash_table_retrieve(ht, limit - i):
            x = hash_table_retrieve(ht, i)
            y = hash_table_retrieve(ht, limit-i)
            if x < y:
                return (y,x)
            else: 
                return (x,y)

    return None
    

   
    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
