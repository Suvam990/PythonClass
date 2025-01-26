category = [
    {'cid':1,'name':'laptop'},
    {'cid':2,'name':'mobile'},
    {'cid':3,'name':'tablet'}
]

product=[
    {'cid':1, 'name':'dell','price':50000,'qty':10},
    {'cid':1, 'name':'mac','price':30000,'qty':30},
    {'cid':2, 'name':'samsung','price':20000,'qty':50},
    {'cid':2, 'name':'iphone','price':40000,'qty':5},   
    {'cid':3, 'name':'mi','price':50000,'qty':10},
]



search = input("Enter category name: ")


for cat in category:
    cat_name = cat['name']
    if cat_name == search:
         cid = cat['cid']
         for  products in product:
              if products['cid'] == cid:
                   print(f'{products['cid']}\t{products['name']}\t{products['price']}\t{products['qty']}')
         