''' u try to withdraw money from a Nigerian ATM.
The ATM has only ₦1000 notes and you have ₦10,000 in your account.
The machine allows withdrawal only if the amount requested is less than or equa    l to your balance.
The user enters the amount. Your  program  should decide:
- Whether to allow the transaction? 
  Or deny it with a message: 
 “Insufficient funds or invalid amount”?
'''

balance = 10000
pay_denomination = 1000

amount = float(input("Enter Amount to withdraw. \n NGN"))

if amount > 0 and amount <= balance:
   if amount % pay_denomination == 0:
      balance -= amount
      print(f"Withdrawing.... \nTransaction Successfull! Your amount is NGN{amount}")
      print(f"Remaining Balance: NGN{balance}")
   else:
      print("Invalid amount. Must be in multiples of NGN1000.")

elif amount > balance:
    print("Insufficient Funds")
							
else:
    print("Amount out of range. Please enter a positive value.")


