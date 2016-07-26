import os

def listContains(list, item):
    for i in list:
        if i == item:
            return True
        return False

class Inventory:
    def __init__(self):
        self.value = 0
        self.items = []
        self.name = ""

    def addItem(self, item):
        self.items.append(item)
        self.value += item.value

    def removeItem(self, item):
        num = 0
        for i in storage.items:
            if i.name == item:
                storage.items.pop(num)
                self.value = 0
                for i in self.items:
                    self.value += i.value
        num += 1

    def setName(self, name):
        self.name = name

class Product:
    def __init__(self):
        self.value = 0

    def setValue(self, price):
        self.value = price

    def setName(self, name):
        self.name = name

storage = Inventory()

def menu():
    os.system("clear")
    print("Inventory Manager")
    print("( View | Add | Remove | Exit )")
    x = raw_input("")
    print()
    if x == "view" or x == "View":
        if len(storage.items) != 0:
            for i in storage.items:
                print "$%i %s" % (i.value, i.name)
            print("Total Value: $%i" % storage.value)
        else:
            print("Nothing to show!")
            raw_input("Press enter to continue")
        raw_input("Press enter to continue")
    elif x == "Exit" or x == "exit":
        quit()
    elif x == "Add" or x == "add":
        name = raw_input("Name: ")
        value = raw_input("Price: ")
        item = Product()
        item.setValue(int(value))
        item.setName(name)
        storage.addItem(item)
        print("Item added!")
        raw_input("Press enter to continue")
    elif x == "Remove" or x == "remove":
        name = raw_input("Name: ")
        storage.removeItem(name)
        print("Item removed!")
        raw_input("Press enter to continue")
    else:
        print("Unknown command!")
        raw_input("Press enter to continue")
    menu()
menu()
