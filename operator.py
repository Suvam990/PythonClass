# # # a = 10
# # # b = 20
# # # print (a+b)

# # # a += b
# # # print(a ) 

# # # a //= b
# # # print(a)

# # # a |= 2
# # # print(a)

# # # a >>= 2
# # # print(a)

# # # a = 20
# # # b =5

# # # print(a+b)
# # # print(a-b)
# # # print(a*b)


# # # # membershiip operator
# # # a = ['omi', 'nirajan', 'subham']
# # # print('omi' not in a)


# # print(3 << 3)
# # print(4^6)
# # # 4=000000000100
# # # 6=000000000110



# # """
# # The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

# # If you push 00 in from the left:
# #  3 = 0000000000000011
# # becomes
# # 12 = 0000000000011000

# # Decimal numbers and their binary values:
# #  0 = 0000000000000000
# #  1 = 0000000000000001
# #  2 = 0000000000000010
# #  3 = 0000000000000011
# #  4 = 0000000000000100
# #  5 = 0000000000000101
# #  6 = 0000000000000110
# #  7 = 0000000000000111
# #  8 = 0000000000001000
# #  9 = 0000000000001001
# # 10 = 0000000000001010
# # 11 = 0000000000001011
# # 12 = 0000000000001100
# # """
# a =5
# b=2
# # print(a/b)
def calculate_tax(amount, tax_rate=13):
    """Calculate tax amount."""
    return (tax_rate / 100) * amount

def display_products():
    """Display available products."""
    print("Available Computers:")
    print("1. Dell - Rs. 20,000")
    print("2. Mac - Rs. 50,000")
    print("3. Toshiba - Rs. 30,000")

def display_packing_options():
    """Display available packing options."""
    print("\nAvailable Packing Options:")
    print("1. No Packing - Rs. 0")
    print("2. Plastic Bag - Rs. 100")
    print("3. Bag - Rs. 2,000")
    print("4. Gift Box - Rs. 3,000")

def display_delivery_options():
    """Display delivery locations."""
    print("\nDelivery Options:")
    print("1. KTM (Kathmandu) - Rs. 1,000")
    print("2. BTK (Bhaktapur) - Rs. 0")
    print("3. LTP (Lalitpur) - Rs. 0")

def main():
    display_products()
    product_choice = int(input("\nChoose a product (1-3): "))
    quantity = int(input("Enter quantity: "))

    # Product Prices
    products = {1: ("Dell", 20000), 2: ("Mac", 50000), 3: ("Toshiba", 30000)}
    product_name, base_price = products[product_choice]
    total_product_cost = base_price * quantity

    # Packing Option
    display_packing_options()
    packing_choice = int(input("\nChoose a packing option (1-4): "))
    packing_costs = {1: 0, 2: 100, 3: 2000, 4: 3000}
    packing_cost = packing_costs[packing_choice]

    # Delivery Option
    display_delivery_options()
    delivery_choice = int(input("\nChoose a delivery location (1-3): "))
    delivery_charges = {1: 1000, 2: 0, 3: 0}
    delivery_charge = delivery_charges[delivery_choice]

    # Tax Calculation
    tax_amount = calculate_tax(total_product_cost)
    
    # Final Total Calculation
    grand_total = total_product_cost + tax_amount + packing_cost + delivery_charge

    # Display Bill
    print("\n--- Final Bill ---")
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Product Cost: Rs. {total_product_cost}")
    print(f"Tax (13%): Rs. {tax_amount}")
    print(f"Packing Cost: Rs. {packing_cost}")
    print(f"Delivery Charge: Rs. {delivery_charge}")
    print(f"\nGrand Total: Rs. {grand_total}")

# Run the program
if __name__ == "__main__":
    main()
