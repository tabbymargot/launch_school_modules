def transactions_for(item_id, transactions_list):
    valid_transactions = []
    for transaction in transactions_list:
        if transaction['id'] == item_id:
            valid_transactions.append(transaction)

    return valid_transactions

def is_item_available(item_id, transactions_list):
    quantities = []

    for transaction in transactions_for(item_id, transactions_list):
        amount = transaction['quantity']
        if transaction['movement'] == 'out':
            amount = -amount
        quantities.append(amount)
    
    return True if sum(quantities) > 0 else False


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True