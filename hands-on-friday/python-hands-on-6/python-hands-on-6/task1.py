'''
#You are given a list of bank transactions:

#transactions = [
 #   {"id": 1, "amount": 200, "type": "deposit"},
  #  {"id": 2, "amount": 50, "type": "withdraw"},
   # {"id": 3, "amount": 500, "type": "deposit"}
#]

#function Signature
#def filter_transactions(transactions, criteria):
   #pass

#Requirement(s):
#The function should return a list of transactions that match the given criteria.

#1. If the criteria is a string field (e.g., "type": "deposit"), return only those transactions with the exact same type.
 #   filter_transactions(transactions, {"type": "deposit"})
# → Returns all deposit transactions

#2.   If the criteria is a numeric field (e.g., "amount": 100), return all transactions where the value is greater than or equal to the given number.

#filter_transactions(transactions, {"amount": 100})
# → Returns all transactions with amount ≥ 100



#Expected Output Examples:
#print(filter_transactions(transactions, {"type": "deposit"}))
#[{'id': 1, 'amount': 200, 'type': 'deposit'},
#{'id': 3, 'amount': 500, 'type': 'deposit'}]
#3
#print(filter_transactions(transactions, {"amount": 100}))
#[{'id': 1, 'amount': 200, 'type': 'deposit'},
#{'id': 3, 'amount': 500, 'type': 'deposit'}]
'''



transactions = [
    {"id": 1, "amount": 200, "type": "deposit"},
    {"id": 2, "amount": 500, "type": "withdraw"},
    {"id": 3, "amount": 500, "type": "deposit"}
]

print(transactions)

def filter_transactions(transactions, criteria):
    key, value = list(criteria.items())[0]
    filtered = []
    for transaction in transactions:
        if type(value) == str:  # check if string → exact match
            if transaction.get(key) == value:
                filtered.append(transaction)
        elif type(value) in (int, float):  # check if numeric >= comparison
            if transaction.get(key, 0) >= value:
                filtered.append(transaction)
    return filtered

print(filter_transactions(transactions, {"type": "deposit"}))
print(filter_transactions(transactions, {"amount": 100}))























'''
   key, value = list(criteria.items())[0]   
   filtered = []
   for transaction in transactions:
      if instance(value, str):   
         if transaction.get(key) == value:
                filtered.append(transaction)
      elif instance(value, (int, float)):  
         if transaction.get(key, 0) >= value:
                filtered.append(transaction)
   return filtered

print(filter_transactions(transactions, {"type": "deposit"}))
print(filter_transactions(transactions, {"amount": 100}))
'''
