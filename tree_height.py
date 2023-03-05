# python3
# 221RDB395 Anastasija Bondare 13.grupa

import sys
import threading

class Node: # Tiek definēta klase Node jeb Mezgls, kas aprakstīs visus mezglus koka struktūrā
    def __list__(self): # Tiek definēts konstruktors
        self.children = [] #Tiek definēts, ka mezgla saraksts ir "children", kas ir sākotnēji ir tukšs, jo nekas netika ievadīts

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

    if "a" in ievade: # Ja ievadītajā tekstā ir "a", tad kods dod atpakaļ gaitu
        return

    if "I" in ievade:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))

    if "F" in ievade:
        ievade = "test/" + input()
        with open(ievade, 'r') as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()