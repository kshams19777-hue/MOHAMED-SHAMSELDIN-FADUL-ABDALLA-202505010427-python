# Import missing modules
import customer
import receipt

def main():
    # Getting the customer data
    name, food, quantity, price, delivery_charges = customer.get_customer()
    
    # Printing out the food receipt
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()