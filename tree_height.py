# python3
# 221RDB395 Anastasija Bondare 13.grupa

import sys
import threading

class Node: # Tiek definēta klase Node jeb Mezgls, kas aprakstīs visus mezglus koka struktūrā
    def  __init__(self): # Tiek definēts konstruktora metode, kas tiek izsaukts, kad tiek definēts jauns objekts no klases
        self.children = [] #Tiek definēts, ka mezgla saraksts ir "children", kas ir sākotnēji ir tukšs, jo nekas netika ievadīts

def compute_height(number, parents): # Tiek definēta jauna fukcija ar diviem parametriem - skaits, vecāki

    nodes = [Node() for i in range(number)] # Tiek izveidots saraksts "nodes", kas glabās elementus tik, cik lietotājs ievadīja ievadē "number"
    root_index = 0 # Koka saknes sākotnējais index ir 0

    for child_index in range(number): # Ar cikla palīdzību pārbauda katru ievadīto elementu ievadītajā "number" diapozonā
        parent_index = parents[child_index] # Atrod vecāka index jeb vietu, kur tas atrodas sarakstā

        if parent_index != -1: # Ar if pārbauda, ja vecāks eksistē,tad 
            nodes[parent_index].children.append(nodes[child_index]) # šim vecākam pievieno klāt bērnu 
        else: # Tomēr, ja neeksistē, tad
            root_index = child_index # apstrādātais elements kļūst par sakni jeb koka virsotni

    return get_height(nodes[root_index]) # Izsaucot funkciju "get_height", tiek aprēķināts koka augstums

def get_height(node):
    if not node.children: # Pārbauda, vai saraksts nav tukšs jeb bērnu tur nav,tad atgriež 1
        return 1
    else: # Tomēr, ja bērni ir sarakstā, tad
        return 1 + max([get_height(child) for child in node.children]) # atrod maksimālo augstumu, kur atrodas bērns un pieskaita 1

# Tiek definēta funkcija "main", kas apstrādās teksta ievadi
def main():
    ievade = input()

    if "a" in ievade: # Ja ievadītajā tekstā ir "a", tad kods dod atpakaļ gaitu
        return

    if "I" in ievade: # Ja ievadītajā tekstā ir "I", tad 
        number = int(input()) # pēc tam ievada elementu skaitu, cik to būs kokā
        parents = list(map(int, input().split())) # ar komandu split atdala elementus viens no otra un skatoties pēc vecāku indeksiem pievieno tiem klāt bērnu
        print(compute_height(number, parents)) # Izvada koka augstumu

    if "F" in ievade: # Ja ievadītajā tekstā ir "F", tad 
        ievade = "test/" + input() # nolasa visu ievadīto ceļu līdz failam,
        with open(ievade, 'r') as file: # nolasa faila saturu un aizver to,
            number = int(file.readline().strip())  # pēc tam nolasa pirmo rindu un pārveido to par Integer jeb skaitli, kas norāda, cik elemntu būs kokā
            parents = list(map(int, file.readline().strip().split())) # un tad otrā rinda arī tiek pārdēvēta par skaitli un atdalīti elementi savā starpā, izmantojot funkciju map()
            print(compute_height(number, parents)) # Izvada koka augstumu

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()