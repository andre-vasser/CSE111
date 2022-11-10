from datetime import datetime
current_date_time = datetime.now()
day_of_week = current_date_time.weekday()
subtotal = float(input("What is your subtotal? "))

## Calculations
discount = subtotal * 0.10 
actual_subtotal = subtotal - discount
sales_tax = subtotal * .06 
discount_sales_tax = actual_subtotal * 0.06
discount_total = actual_subtotal + discount_sales_tax
non_discount_total = sales_tax + subtotal

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2) : 
    print(f'Discount amount ${discount:.2f}')
    print(f"Sales Tax: ${discount_sales_tax:.2f}")
    print(f'Total: ${discount_total:.2f}')
else: 
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: {non_discount_total:.2f}")




