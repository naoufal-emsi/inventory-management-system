# core/inventory_ops.py
from data.inventory_data import products

def add_product(product):
    products.append(product)

def update_product(product_id, new_data):
    for product in products:
        if product['id'] == product_id:
            product.update(new_data)
            break

def delete_product(product_id):
    global products
    products = [product for product in products if product['id'] != product_id]

def search_product_by_name(name):
    return [product for product in products if name.lower() in product['name'].lower()]

def sort_products_by(field):
    return sorted(products, key=lambda x: x.get(field))

def list_all_products():
    return products
