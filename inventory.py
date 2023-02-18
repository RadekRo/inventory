import csv, os

a = {"torch": 1, "sword": 2, "helmet": 1, "shield": 4, "boots": 1}
b = {}
c = ("torch", "sword", "staff", "wand")
d = ("sword", "sword", "staff")

def display_inventory(inventory):
    for item in inventory:
        print(f"{item}: {inventory[item]}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    print(inventory)

def remove_from_inventory(inventory, removed_items):
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] == 0:
                del inventory[item]
    print(inventory)

def select_value_of_key(item):
    return item[1]

def print_table(inventory, order):
    print("""
-----------------
item name | count
-----------------""")
    order = order.replace(" ", "")
    if order == "empty":
        for item in inventory:
            print(f"{item} | {inventory[item]}")
    elif order == "count,asc":
        sorted_dictionary = sorted(inventory.items(), key=select_value_of_key)
        for item in sorted_dictionary:
            print(f"{item[0]} | {item[1]}")
    elif order == "count,desc":
        sorted_dictionary = sorted(inventory.items(), key=select_value_of_key)
        reversed_dictionary = sorted_dictionary[::-1]
        for item in reversed_dictionary:
            print(f"{item[0]} | {item[1]}")

def import_inventory(inventory, filename = "import_inventory.csv"):
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            csvreader = csv.reader(file, skipinitialspace=True)
            for row in csvreader:
                for i in range(0, len(row)):
                    if row[i] in inventory:
                        inventory[row[i]] += 1
                    else:
                        inventory[row[i]] = 1
        print(inventory)
    else:
        print(f"File '{filename}' not found!")
            
def export_inventory(inventory, filename = "export_inventory.csv"):
    export_data = []
    for item in inventory:
        for i in range(0, inventory[item]):
            export_data.append(item)
    try:
        with open(filename, "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(export_data)
        print("Data export done!")
    except:
        print(f"You don't have permission creating file '{filename}'!")


#TESTS
print("""CURRENT DATA FOR TESTS:
a = {"torch": 1, "sword": 2, "helmet": 1, "shield": 4, "boots": 1}
b = {}
c = ("torch", "sword", "staff", "wand")
d = ("sword", "sword", "staff")
""")
print("DISPLAY INVENTORY\n******************")
display_inventory(a)
display_inventory(b)
print(f"\nADD TO INVENTORY {a}\nTHIS DATA: {c}\n******************\nRESULT: ")
add_to_inventory(a, c)
print(f"\nREMOVE FROM INVENTORY {a}\nTHIS DATA: {d}\n******************\nRESULT: ")
remove_from_inventory(a, d)
print(f"\nPRINT TABLE\nFROM DATA: {a}\n******************")
print("\nARGUMENT: EMPTY *****")
print_table(a, "empty")
print("\nARGUMENT: COUNT, DESC *****")
print_table(a, "count, desc")
print("\nIMPORT INVENTORY FROM EXISTING FILE\n")
print("FILE data: ruby, rope, ruby, gold, coin, axe\n******************\nRESULT: ")
import_inventory(a)
print("\nIMPORT FROM FILE THAT NOT EXISTS *****")
import_inventory(a, "inventory.csv")
print("\nEXPORT INVENTORY\n******************")
print("WITH PERMISSION ***")
export_inventory(a)
print("\nWITHOUT PERMISSION ***")
export_inventory(a, "/export.csv")