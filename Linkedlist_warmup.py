
'''Start with a head and a tail.
find size.'''


def remove_duplicates(self):
    # set current head
    current_node = self.head
    # is the list is not empty
    if current_node is None:
        return
    # loop while there are nodes
    while current_node.next is not None:
        # if the data is equal to the next nodes data
        if current_node.data == current_node.next.data:
            #
            next_next = current.next.next
            current.next = next.next
        else:
            current_node = current.next
    return self.head
