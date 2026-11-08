print("=== Parking Garage Calculator ===")
print("Enter day type: weekday, weekend, or holiday")
print("Type 'done' when finished entering hours")

running_total=0.0

while True:
    day_type=input("Enter day type for 1 hour: ").strip().lower()

    if day_type=="done":
        print()
        break

    if day_type=="weekday":
        price=8.00
        running_total+=price
        print(f"Price: {price:.2f}")
        print(f"Current total: {running_total:.2f}\n")
    elif day_type=="weekend":
        price=6.00
        running_total+=price
        print(f"Price: {price:.2f}")
        print(f"Current total: {running_total:.2f}\n")
    elif day_type=="holiday":
        price=5.00
        running_total+=price
        print(f"Price: {price:.2f}")
        print(f"Current total: {running_total:.2f}\n")
    else:
        print("Invalid day type! Please enter weekday, weekend, holiday, or done")

discount=0.0
if running_total>=50.00:
    discount=7.00

final_total=running_total-discount

print("=== Parking Summary ===")
print(f"Subtotal: ${running_total:.2f}")
if discount>0:
    print(f"Frequent Parker Discount: -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for parking with us!")