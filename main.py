# concept and coding idea is from the book "Programminger Bolod To Boss" -by Jhankar Mahbub
# implemented and modified in python 3 by me(Adnan Alam)



class Store:
    
    def __init__(self,name):
        
        self.name = name
        self.items = []
        self.prices = {}
        self.stock = {}
        self.totalSales = 0
    
    
    def addItem(self,name,quantity,price=None):
        
        isAvailable = self.isItemAvailable(name)
        
        if isAvailable == True:
            self.stock[name] += quantity
        else:
            self.items.append(name)
            self.prices[name] = price
            self.stock[name] = quantity
    
        
    def isItemAvailable(self,name):
        
        if name in self.items:
            return True
        else:
            return False
    
    
    def getPrice(self,name):
        
        isAvailable = self.isItemAvailable(name)
        
        if isAvailable == True:
            itemPrice = self.prices[name]
            return itemPrice
        else:
            print("Item isn't in the Stock!") 
    
    
    def sellItem(self,name,quantity):
        
        isAvailable = self.isItemAvailable(name)
        
        if isAvailable == True:
            available = self.stock[name]

            if available < quantity:
                print("We don't have enough.") 
            else:
                itemPrice = self.getPrice(name)
                currentSale = itemPrice * quantity
                self.totalSales += currentSale
                self.stock[name] -= quantity
        else:
            print("We don't have this item.") 
            

    
    def getStock(self):
        
        print("Stock")
        print("-" * 10)
        print()
        
        for item, quantity in self.stock.items():
            print("{} : {}".format(item,quantity))
    
    
    def removeItem(self,name):
        
        self.items.remove(name)
        del self.prices[name]
        del self.stock[name]
        
    
    def getTotalSales(self):
        
        print("Total Sales: {}".format(self.totalSales))


my_store = Store("Store's name goes here")
