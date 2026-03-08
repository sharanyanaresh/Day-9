from collections import namedtuple

Product = namedtuple("Product", ["id","name","category","price"])

catalog = [
Product(1,"Laptop","Electronics",75000),
Product(2,"Phone","Electronics",50000),
Product(3,"Headphones","Electronics",5000),
Product(4,"TShirt","Clothing",1200),
Product(5,"Jeans","Clothing",2500),
Product(6,"Jacket","Clothing",4000),
Product(7,"Clean Code","Books",700),
Product(8,"Python Crash Course","Books",800),
Product(9,"Atomic Habits","Books",650),
Product(10,"Chair","Home",3000),
Product(11,"Table","Home",7000),
Product(12,"Lamp","Home",1500),
Product(13,"Monitor","Electronics",20000),
Product(14,"Notebook","Books",300),
Product(15,"Sofa","Home",25000)
]

customer_1_cart = {catalog[0],catalog[6],catalog[9]}
customer_2_cart = {catalog[1],catalog[6],catalog[10]}
customer_3_cart = {catalog[0],catalog[7],catalog[11]}
customer_4_cart = {catalog[2],catalog[6],catalog[12]}
customer_5_cart = {catalog[0],catalog[6],catalog[13]}

all_carts = [customer_1_cart,customer_2_cart,customer_3_cart,customer_4_cart,customer_5_cart]

# Bestsellers
bestsellers = set.intersection(*all_carts)
print("Bestsellers:",bestsellers)

# Catalog reach
reach = set.union(*all_carts)
print("Catalog Reach:",reach)

# Exclusive purchases
others = customer_2_cart | customer_3_cart | customer_4_cart | customer_5_cart
exclusive = customer_1_cart - others
print("Exclusive to customer1:",exclusive)

def recommend_products(customer_cart,all_carts):
    other_products = set.union(*all_carts)
    return other_products - customer_cart

print("Recommendations:",recommend_products(customer_1_cart,all_carts))

def category_summary():
    categories = set(p.category for p in catalog)
    return {c:{p.name for p in catalog if p.category==c} for c in categories}

print("Category Summary:",category_summary())