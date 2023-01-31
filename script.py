## Part 1

def studentDiscount(price): ## Function number 1 is for student discount which discounts the current price by 10%.
    return (price*0.9)

def returnShopperDiscount(price):## Function number 2 is for an additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
    return (price*0.95)

## Part 2
## Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
x = lambda a : (a*((a * 5)**2))
print("x*(x+5)^2 = " + x(5) + " where x= 5")
## Part 3

prices = [12, 14, 8, 100]

def discount(price):
    return (price - (price*0.1))


map(discount, prices)
## Part 4

class Computer: 
    ##Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.
    # You can use any specifications that you want.
    cpu=""
    ram=""
    storage=""

    def getspecs(self):
        self.cpu = input("Please enter CPU: ")
        self.ram = input("Please enter how many GB of RAM: ")
        self.storage = input("Please enter how many GB of Storage: ")

    def displaySpecs(self):
        print("CPU : " + self.cpu)
        print("GB of RAM : " + self.ram)
        print("GB of Storage : " + self.storage)


class Desktop(Computer): 
    graphicsCard=""

    def getspecs(self):
        self.graphicsCard=input("Please enter Graphics Card: ")
    def displaySpecs(self):
        print("GPU : " + self.graphicsCard)


class Laptop(Computer):
    battery=""

    def getspecs(self):
        self.battery=input("Please enter Battery Hours: ")
    def displaySpecs(self):
        print("Battery Hours : " + self.battery)

myLaptop = Laptop()
myDesktop = Desktop()

myLaptop.getspecs()
myDesktop.getspecs()

myLaptop.displaySpecs()
myDesktop.displaySpecs()

## Part 5

class weirdMath:
    x=0
    def __mul__(self, other):
        x =  self.x + other.x
        return x

