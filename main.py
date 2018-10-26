# concept and coding idea is from the book "Programminger Bolod To Boss" -by Jhankar Mahbub
# http://habluderadda.com/concepts/app/storeManager.html

# implemented and modified in python 3 by me(Adnan Alam)



class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.prices = {}
        self.stock = {}
        self.discounts = {}
        self.total_sales = 0

    def add_item(self, name, quantity, price=None, discount=None):
        is_available = self.is_item_available(name)

        if discount is not None:
            self.discounts[name] = discount

        if is_available == True:
            self.stock[name] += quantity
        else:
            self.items.append(name)
            self.prices[name] = price
            self.stock[name] = quantity

    def is_item_available(self, name):
        if name in self.items:
            return True
        else:
            return False

    def get_price(self, name):
        is_available = self.is_item_available(name)

        if is_available == True:
            item_price = self.prices[name]
            return item_price
        else:
            print("Item isn't in the Stock!")

    def sell_item(self, name, quantity):
        is_available = self.is_item_available(name)

        if is_available == True:
            available = self.stock[name]
            if available < quantity:
                print("We don't have enough.")
            else:
                if name in self.discounts.keys():
                    discount = self.discounts[name]
                    item_price = self.get_price(name)
                    total_discount = (item_price * discount) * quantity
                    current_sale = (item_price * quantity) - total_discount
                    self.total_sales += current_sale
                    self.stock[name] -= quantity
                    print("Total Discount: {}".format(total_discount))
                else:
                    item_price = self.get_price(name)
                    current_sale = item_price * quantity
                    self.total_sales += current_sale
                    self.stock[name] -= quantity

            print("Total Price: {}".format(current_sale))
        else:
            print("We don't have this item.")

    def get_stock(self):
        print("Stock")
        print("-" * 10)
        print(" ")
        for item, quantity in self.stock.items():
            print("{} : {}".format(item, quantity))

    def remove_item(self, name):
        self.items.remove(name)
        del self.prices[name]
        del self.stock[name]

    def get_total_sales(self):
        print("Total Sales: {}".format(self.total_sales))

        

my_store = Store("Test Store")


