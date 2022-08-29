# Ecommerce system using functions and arguments, dictionaries and lists, and loops

my_shop = {}


def create_products_container():
    # Create a dictionary to store products
    # check if products container exists
    if 'products' in my_shop:
        print('Products container already exists')
        return my_shop['products']
    else:
        my_shop['products'] = {}
        print('Products container created')
        return my_shop['products']


def create_product(products, product_name, product_price):
    # Create a product
    # check if product exists
    if product_name in products:
        print('Product already exists')
        return products
    else:
        products[product_name] = product_price
        print('Product created')
        return products


def update_product(products, product_name, product_price):
    # Update a product
    # check if product exists
    if product_name in products:
        products[product_name] = product_price
        print('Product updated')
        return products
    else:
        print('Product does not exist')
        return products


def delete_product(products, product_name):
    # Delete a product
    # check if product exists
    if product_name in products:
        del products[product_name]
        print('Product deleted')
        return products
    else:
        print('Product does not exist')
        return products


def show_products(products):
    # Show all products
    for product in products:
        print(product, ':', products[product])


def show_product(products, product_name):
    # Show a product
    if product_name in products:
        print(product_name, ':', products[product_name])
    else:
        print('Product does not exist')



def main():
    # Create a products container
    products = create_products_container()
    
    while True:
        # Show menu
        print('1. Create a product')
        print('2. Update a product')
        print('3. Delete a product')
        print('4. Show all products')
        print('5. Show a product')
        print('6. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            # Create a product
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            products = create_product(products, product_name, product_price)
        elif choice == '2':
            # Update a product
            product_name = input('Enter product name: ')
            product_price = input('Enter product price: ')
            products = update_product(products, product_name, product_price)
        elif choice == '3':
            # Delete a product
            product_name = input('Enter product name: ')
            products = delete_product(products, product_name)
        elif choice == '4':
            # Show all products
            show_products(products)
        elif choice == '5':
            # Show a product
            product_name = input('Enter product name: ')
            show_product(products, product_name)
        elif choice == '6':
            # Exit
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()