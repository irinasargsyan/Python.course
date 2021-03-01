from Productcheck import check

def buy(product,num,price):
    if check(product, num) == True:
        return "You bought" + " " + str(product) + " " + "and spent" + " " + str(num*price)
    else:
        return "Sorry! Weare out of this product."
    
def main():
    buy("candy", 5, 5)