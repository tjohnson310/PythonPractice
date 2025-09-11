class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("Previous node not in list. Insertion not possible...")
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        last_node = self.head
        while last_node.next:
            if last_node.data == prev_node:
                next_node = last_node.next
                new_node.next = next_node
                curr = last_node
                curr.next = new_node
                return
            last_node = last_node.next

    def delete(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            return

        prev.next = curr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.prepend("E")
    llist.insert("B", "Z")
    llist.delete("E")
    llist.print_linked_list()
