class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head= None
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
    # def add_after_node(self, data, key):
    #     cur = self.head
    #     while cur:
    #         if cur.next is None and cur.data == key:
    #             self.append(data)
    #             return
    #         elif cur.data == key:
    #             new_node = Node(data)
    #             nxt = cur.next
    #             cur.next = new_node
    #             new_node.next = nxt
    #             new_node.prev = cur
    #             nxt.prev = new_node
    #             return
    #         cur = cur.next
    # def add_before_node(self, data , key):
    #     cur = self.head
    #     while cur:
    #         if cur.next is None and cur.data == key:
    #             self.append(data)
    #             return
    #         elif cur.data == key:
    #             new_node = Node(data)
    #             prev = cur.prev
    #             prev.next = new_node
    #             cur.prev = new_node
    #             new_node.next = cur
    #             new_node.prev = prev
    #             return
    #         cur = cur.next
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


DoublyLL= DoublyLinkedList()
DoublyLL.append("B")
DoublyLL.append("A")
