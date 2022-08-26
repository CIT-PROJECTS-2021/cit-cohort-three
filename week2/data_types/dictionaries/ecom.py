# An ecommerce program in python using dictionaries

products = {
    "1": {"name": "Laptop", "price": 15000.0, "quantity": 10},
    "2": {"name": "Phones", "price": 400.0, "quantity": 300}
}


while True:
    print("1. Add a product \n2. Delete a product\n3. List Products \n4. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_qty = int(input("Enter product quantity: "))

        if product_id in products:
            print("Sorry, Product ID already exists")
            break
        products[product_id] = {
            "name": product_name,
            "price": product_price,
            "quantity": product_qty
        }

    elif option == "2":
        product_id = input("Enter product ID: ")
        if product_id in products:
            del products[product_id]
        else:
            print(f"Product not found")

    elif option == "3":
        for product_id, product_details in products.items():
            print(f"Product ID: {product_id},\
             Product name: {product_details['name']},\
            Price: {product_details['price']},\
            Quantity: {product_details['quantity']}")
    
    elif option == "4":
        print(f"Closing program")
        break

    else:
        print("Invalid option")