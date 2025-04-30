# core/stock_monitor.py
from data.inventory_data import products

def get_low_stock_products(threshold):
    return [product for product in products if product['quantity'] <= threshold]

def auto_restock(min_level, restock_to):
    for product in products:
        if product['quantity'] < min_level:
            product['quantity'] = restock_to

def calculate_stock_value():
    return sum(product['price'] * product['quantity'] for product in products)

def get_inventory_by_category():
    inventory_by_category = {}
    for product in products:
        category = product['category']
        if category not in inventory_by_category:
            inventory_by_category[category] = []
        inventory_by_category[category].append(product)
    return inventory_by_category
