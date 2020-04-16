'''two discounts, one 10% the other 5%
crate functions to apply the discounts to a price,
create a function to apply both discounts'''

products = {
'orange': 200,
'apple': 100,
'carrot': 250,
'letuce': 145,
}

def ten_percent(x):
    discounted = (10 * x)/100
    result = x - discounted
    return result

ten_percent(200)

def five_percent(x):
    discounted = (5 * x)/100
    result = x - discounted
    return result

five_percent(200)

'''using both functions at the same time to apply to a number'''
number = 200
print (type(five_percent(five_percent(number))))

def both_discounts(x):
    discounted = (15 * x)/100
    result = x - discounted
    print(result)

def cashier():
    x = str(input('please choose your product: '))
    y = str(input('Are you a student y/n: '))
    z = str(input('Are you a regular customer y/n: '))
    product = products.get(x,'not found')
    if y == 'y' and z == 'n':
        print(ten_percent(product))
    elif y == 'y' and z == 'y':
        print(both_discounts(product))
    elif y == 'n' and z =='y':
        print(type(five_percent(product)))
    else:
        print(product)

cashier()

'''DISCOUNT TO ALL VALUES'''

product_prices = [100,200,300,400,500]

def discount(price):
    price = price - (price * 10)/100
    return price

updated_prices = list(map(discount,product_prices))
print(updated_prices)
