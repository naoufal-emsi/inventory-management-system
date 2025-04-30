# core/transaction_ops.py
from data.inventory_data import products
from data.transactions import transactions
from datetime import datetime

def sell_product(product_id, quantity):
    for product in products:
        if product['id'] == product_id and product['quantity'] >= quantity:
            product['quantity'] -= quantity
            transactions.append({
                "type": "sale",
                "product_id": product_id,
                "quantity": quantity,
                "price": product['price'],
                "date": datetime.today().strftime('%Y-%m-%d')
            })
            break

def purchase_product(product_id, quantity, cost):
    for product in products:
        if product['id'] == product_id:
            product['quantity'] += quantity
            transactions.append({
                "type": "purchase",
                "product_id": product_id,
                "quantity": quantity,
                "price": cost,
                "date": datetime.today().strftime('%Y-%m-%d')
            })
            break

def view_transaction_history():
    return transactions
