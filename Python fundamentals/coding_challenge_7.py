products = {
'apple': 100,
'banana': 250,
'raspberry': 390
}

print(products)

def ask_price():
    x = input('Insert the name of the item: ')
    if x in products:
      print(products.get(x))

ask_price()

products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
