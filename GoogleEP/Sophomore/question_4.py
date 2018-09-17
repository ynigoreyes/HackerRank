class LinkedList:
    def __init__(self, Node):
        this.head = Node

class Node:
    def __init__(self, x):
        this.val = x
        this.next = null

def altLinkedList(LinkedList):
    head = LinkedList.head
    arr = []

    # Pushes values to an array
    while head is not None:
        arr.push(head.val)
        head = head.next

    # If a single node was given as the arguement
    if len(arr) <= 1:
        return LinkedList(Node(arr.pop()))

    # Creates a head for the new linked list
    ans = LinkedList()
    ans.head = Node(arr.pop(0))
    current = ans.head.next

    flag = 'left'

    # Alternate between left and right based on a flag
    while len(arr) != 0:
        if flag == 'left':
            current = Node(arr.pop(0))
            current = current.next
            flag = 'right'
        else:
            current = Node(arr.pop())
            current = current.next
            flag = 'left'


    return ans

