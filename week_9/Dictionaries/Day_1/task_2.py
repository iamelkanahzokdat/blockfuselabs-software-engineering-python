customer = {
    "name":  "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False,
}

discount = 0
freebie = None

if customer["loyalty_card"]:
   discount += 10
   print(f"You got {discount}% discount, loyalty card holder!")   

# Additional 5% if order is above 20,000
if customer["order_amount"] > 20000:
   discount += 5
   print(f"You got an additional {discount}% discount for ordering above 20,000NGN")

# Non-loyalty customers with large orders get a free soft drink

else:
   freebie = "Free Soft Drink"
   print(f"{freebie} cause you dont have a loyalty card")

   print(discount)

# Calculate discounted price
final_price = customer["order_amount"] * (1 - discount / 100)

# Create summary
order_summary = {
    "customer_name": customer["name"],
    "original_amount": customer["order_amount"],
    "discount_applied": f"{discount}%",
    "final_price": customer["order_amount"] * (1 - discount / 100),
    "freebie": freebie
}

# Print summary for cashier
print("=== Order Summary ===")
print(f"Customer: {order_summary['customer_name']}")
print(f"Original Amount: ₦{order_summary['original_amount']}")
print(f"Discount: {order_summary['discount_applied']}")
print(f"Final Price: ₦{order_summary['final_price']}")

if freebie:
    print(f"Freebie: {freebie}")
 


