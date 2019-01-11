
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            dummy = self.head
            while dummy.next:
                dummy = dummy.next

            dummy.next = Node(val)

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        dummy = self.head
        while dummy:
            count += 1
            dummy = dummy.next
        return count

    #  by index
    def delete_idx(self, idx):
        if idx < 0:
            return "impossible"
        elif idx >= self.get_length():
            return "Index is too high"

        if idx == 0:
            self.head = self.head.next
            return

        counter = 0
        dummy = self.head
        while dummy:
            if counter + 1 == idx:
                next_node_to_skip = dummy.next
                dummy.next = next_node_to_skip.next
                return
            counter += 1
            dummy = dummy.next

    #  boolean returned
    def search(self, val):
        if self.head is None:
            return False
        dummy = self.head
        while dummy:
            if dummy.val == val:
                return True

            dummy = dummy.next

        return False

    #  return string of linked list
    def __repr__(self):
        ret = ""
        dummy = self.head
        while dummy:
            ret += f"{dummy.val} => "
            dummy = dummy.next

        return ret


class Stack:

    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return "empty stack"
        value = self.top.val
        self.top = self.top.next

        return value

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def __repr__(self):
        ret = ""
        dummy = self.top
        while dummy:
            ret += f"{dummy.val}--"
            dummy = dummy.next

        return ret


#  enqueue (pushing) works on the back
#  dequeue (pop) works on the front
#  this makes sense due to First In First Out Ordering Principle
#  self.front node => node 3 => node 4 => self.back node
#  dequeue gets self.front node 3 => node 4 => self.back node
class Queue:

    def __init__(self):
        self.back = None
        self.front = None

    def enqueue(self, val):
        new_node = Node(val)
        if self.back:
            self.back.next = new_node
        self.back = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        if self.front is None:
            return "empty queue"
        val = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.back = None

        return val


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.insert_helper(self.root, val)

    def insert_helper(self, curr_node, val):
        if val < curr_node.val:
            if curr_node.left is None:
                curr_node.left = TreeNode(val)
            else:
                self.insert_helper(curr_node.left, val)
        elif val > curr_node.val:
            if curr_node.right is None:
                curr_node.right = TreeNode(val)
            else:
                self.insert_helper(curr_node.right, val)

    #  return boolean based on if val is in BST
    def search(self, val):
        return self.search_helper(self.root, val)

    def search_helper(self, curr_node, val):
        if curr_node is None:
            return False
        elif curr_node.val == val:
            return True
        elif val < curr_node.val:
            return self.search_helper(curr_node.left, val)
        elif val > curr_node.val:
            return self.search_helper(curr_node.right, val)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)


def pre_order(node):
    if node:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)


def test_bst():
    b = BST()
    b.insert(10)
    b.insert(5)
    b.insert(20)
    b.insert(8)
    b.insert(2)
    print("True", b.search(10))
    print("True", b.search(2))
    print("False", b.search(100))

    print("\nPre-Order\n")
    pre_order(b.root)
    print("\nIn-Order\n")
    in_order(b.root)
    print("\nPost-Order\n")
    post_order(b.root)


def main():
    l1 = LinkedList()
    print(l1)
    l1.add(1)
    l1.add(2)
    l1.add(3)
    l1.add(4)
    print(l1)
    print("4", l1.get_length())
    print("False: ", l1.search(0))
    print("True: ", l1.search(3))

    #  1 3 4
    l1.delete_idx(1)

    print(l1)

    # 3 4
    l1.delete_idx(0)

    print(l1)
    print("2", l1.get_length())

    print("\n---------\n")
    s1 = Stack()
    print("True", s1.is_empty())
    s1.push(5)
    s1.push(4)
    s1.push(3)
    s1.push(2)
    print("False", s1.is_empty())
    print(s1)

    print("2", s1.pop())
    s1.pop()
    s1.pop()
    print(s1)
    s1.pop()
    print(s1)
    print(s1.pop())


def binary_search(a_list, val):

    start = 0
    end = len(a_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if a_list[mid] == val:
            return True
        elif a_list[mid] > val:
            end = mid - 1
        elif a_list[mid] < val:
            start = mid + 1

    return False


def test_search():
    t1 = [1, 2, 3, 4, 5, 6, 7, 8]
    t2 = [2, 7, 19, 20, 100]

    print("True: ", binary_search(t1, 1))
    print("True: ", binary_search(t1, 6))
    print("True: ", binary_search(t1, 8))
    print("False: ", binary_search(t1, 100))
    print("False: ", binary_search(t2, 5))
    print("False: ", binary_search(t2, 78))
    print("True: ", binary_search(t2, 7))

