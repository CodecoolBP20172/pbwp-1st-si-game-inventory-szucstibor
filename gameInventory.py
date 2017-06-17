# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import operator
import csv
import sys
_inventory = {"fucks given": 0, "shit": 1, "stack": 1}
addedItems = []
total = 0
imported_inventory = []
i = 0
# Displays the inventory.


def decor(func):
    def wrap():
        print("==========================")
        func()
        print("==========================")
    return wrap


def displayInventory(inventory):
    total = 0
    for k, v in _inventory.items():
        print('{:>0}  {:>12}'.format(v, k))
        total = total + v
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


def print_table(inventory, order=None):
    if order is None:
        displayInventory(inventory)
    elif order is "count,asc":
        sorted(_inventory.items(), key=operator.itemgetter(1))
        displayInventory(inventory)
    elif order is "count,desc":
        sorted(_inventory.items(), key=operator.itemgetter(1), reverse=True)
        displayInventory(inventory)


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
    with open("export_inventory.csv", 'rb') as _inventory:
        wr = csv.writer(_inventory)
        wr.writerow(_inventory)

import_inventory(_inventory, filename="import_inventory.csv")
decorated = decor(print_table(_inventory, order=None))
decorated()
