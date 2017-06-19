# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import operator
import csv
import sys
import os
_inventory = {}
addedItems = []
total = 0
i = 0
ordering = ""
sorted_inventory = []
s = [(k, _inventory[k]) for k in sorted(_inventory, key=_inventory.get, reverse=True)]

# Displays the inventory.


def displayInventory(inventory):
    total = 0
    print("Inventory: ")
    print("Count   Item name")
    print("------------------------------")
    for k, v in _inventory.items():
        print('{:>2}  {:>12}'.format(v, k))
        total = total + v
    print("------------------------------")
    print("Total number of items: ", total)

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, addedItems):
    for i in range(len(addedItems)):
        _inventory.setdefault(addedItems[i], 0)
        _inventory[addedItems[i]] = _inventory[addedItems[i]]+1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order):
    global _inventory
    global total
    if ordering == "count,asc":
        inventory_asc = sorted(_inventory.items(), key=operator.itemgetter(1))
        print("Inventory: ")
        print("Count   Item name")
        print("------------------------------")
        for i in range(len(inventory_asc)): 
            print('{:>2}  {:>12}'.format(inventory_asc[i][1], inventory_asc[i][0]))
        print("------------------------------")
        print("Total number of items: ", total)

    elif ordering == "count,desc":
        inventory_desc = sorted(_inventory.items(), key=operator.itemgetter(1), reverse=True)
        print("Inventory: ")
        print("Count   Item name")
        print("------------------------------")
        for i in range(len(inventory_desc)):
            print('{:>2}  {:>12}'.format(inventory_desc[i][1], inventory_desc[i][0]))
        print("------------------------------")
        print("Total number of items: ", total)

    elif ordering == "":
        displayInventory(_inventory)
# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile)
        addedItems = list(reader)
        add_to_inventory(_inventory, addedItems[0])

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    with open("export_inventory.csv", 'w') as export:
        for k, v in inventory.items():
            if v > 0:
                for i in range(v):
                    export.write(k)
                    export.write(",")
                else:
                    export.write(k)
                    export.write(",")
    export.close()

import_inventory(_inventory, filename="import_inventory.csv")
ordering = (input(""))
export_inventory(_inventory, filename="export_inventory.csv")
print_table(_inventory, ordering)