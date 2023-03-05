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
    # Nolasīt mezglu skaitu no standarta ievades
    n = int(input())

    # Nolasīt vecāku indeksu sarakstu no standarta ievades un sadalīt to pa atsevišķiem skaitļiem
    parents = list(map(int, input().split()))

    # Izvadīt koka augstumu uz ekrāna
    print(compute_height(n, parents))

    # Noteikt datu avotu - standarta ievade vai fails
    if "I" in input().strip():
        source = (int(input()), list(map(int, input().split())))
    elif "F" in input().strip():
        with open("test/" + input().strip(), 'r') as f:
            source = (int(f.readline().strip()), list(map(int, f.readline().strip().split())))

        # Aprēķināt koka augstumu, izmantojot funkciju compute_height
        max_height = compute_height(*source)

        # Izvadīt koka augstumu uz ekrāna
        print(max_height)

# Pārbaudīt, vai tiek izsaukts fails, nevis standarta ievade
if __name__ == "__main__":
    # Palielināt rekursijas maksimālo dziļumu
    sys.setrecursionlimit(10**7)

    # Izveidot jaunu pavedienu un izsaukt galveno funkciju
    threading.stack_size(2**27)
    threading.Thread(target=main).start()
