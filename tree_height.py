# python3
# 221RDB395 Anastasija Bondare 13.grupa

import sys
import threading

class Node:
    def __init__(self):
        self.children = []

def compute_height(n, parents):
    nodes = [Node() for i in range(n)]
    root_index = 0
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root_index = child_index
        else:
            nodes[parent_index].children.append(nodes[child_index])
    return get_height(nodes[root_index])

def get_height(node):
    if not node.children:
        return 1
    else:
        return 1 + max([get_height(child) for child in node.children])

def main():
    ievade = input()
    If "a" in ievade: # Ja ievadītajā tekstā ir "a", tad kods dod atpakaļ gaitu
        return
    If "I\r" in ievade:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
