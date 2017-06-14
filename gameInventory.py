# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
total = 0
loot = []
# Displays the inventory.


def displayInventory(inventory):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        total = total + v
    print("Total number of items: ", total)

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]]+1
    print(inventory)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    for key, value in len(inventory):
        print("%10.2f    %10.2f" % key, value)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
