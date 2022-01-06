class MenuItem:
    def __init__(self, item, type, price):
        self.item = item
        self.type = type
        self.price = price


class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.menu.sort(key=lambda x: x.price)
        self.orders = []

    def cheapestitem(self):
        print(self.menu[0].price)

    def addorder(self, itemName):
        itemLookup = next((x for x in self.menu if x.item == itemName), None)
        if itemLookup is not None:
            print(itemLookup.item + " added!")
            self.orders.append(itemLookup)  # Append automatically adds to end of list
        else:
            print("This item is currently unavailable!")


    def fulfillorder(self):
        if len(self.orders) != 0:
            self.orders.pop(0)
        else:
            print("All orders fulfilled.")


    def listorders(self):
        print("Printing List: ")
        if len(self.orders) != 0:
            for x in self.orders:
                print(x.item)
        else:
            print("Currently no orders.")
    def dueammount(self):
        sum = 0.0
        for x in self.orders:
            sum += x.price
        print("Total due: $%.2f" % sum)
        return sum

    def drinksonly(self):
        print("Listing only drinks...")
        for x in self.menu:
            if x.type == "drink":
                print(x.item)

    def foodonly(self):
        print("Listing only food...")
        for x in self.menu:
            if x.type == "food":
                print(x.item)


item1 = MenuItem("Coffee", "drink", 4.99)
item2 = MenuItem("Cake Pop", "food", 2.99)
item3 = MenuItem("Lemonade", "drink", 3.50)
item4 = MenuItem("Water", "drink", 1.50)
itemList = [item1, item2, item3, item4]


testShop = CoffeeShop("CharBux", itemList)
testShop.cheapestitem()
testShop.addorder("Coffee")
testShop.addorder("Latte")
testShop.addorder("Cake Pop")
testShop.dueammount()
testShop.drinksonly()
testShop.foodonly()
testShop.listorders()
testShop.fulfillorder()
testShop.listorders()
testShop.fulfillorder()
testShop.listorders()
testShop.fulfillorder()