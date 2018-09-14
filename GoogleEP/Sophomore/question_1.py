# Time Complexity: O(n)
# Space Complexity: O(n)
def main(LinkedList):
    """
    class Node {
        this.val = x
        this.next = Node
    }
    class LinkedList {
        this.head = Node
    }
    """
    temp = LinkedList.head

    # Delete all of the heads that will be greater than 100
    while (temp and temp.val > 100):
        LinkedList.head = temp.next
        temp = LinkedList.head

    while temp:
        while temp and temp.val <= x: # Search for > 100
            temp = temp.next
            prev = prev.next

        if !temp: # If we went through the whole list
            return LinkedList

        # Make both pointers point to the same thing. AKA delete
        prev.next = temp.next

        temp = prev.next

    return LinkedList


