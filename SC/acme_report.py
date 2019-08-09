# Imports
from acme import Product
import random as rand

# Word bank to create products
prefix = ['Awesome', 'Shiny', 'Impressive',
          'Portable', 'Improved']
suffix = ['Anvil', 'Catapult', 'Disguise',
          'Mousetrap', '???']

# Generate random products
def generate_products(count=30):
    # Create a list of names
    product_names = [rand.choice(prefix) + ' ' + rand.choice(suffix) for i in range(count)]

    # Use Product class to create a list of products
    products = [Product(name) for name in product_names]

    # Change default values
    for prod in products:
        prod.weight = rand.randint(5, 100)
        prod.price = rand.randint(5, 100)
        prod.flammability = rand.uniform(0.0, 2.5)

    return products

# Print an inventory report
def inventory_report(products):
    print('SUPER OFFICIAL ACME REPORT')
    print('')

    # find unique product names
    names = [prod.name for prod in products]
    print("There are", len(set(names)), 'unique products.')
    print('')

    # Send numerical vars to lists as well
    prices = [prod.price for prod in products]
    weights = [prod.weight for prod in products]
    flammabilities = [prod.flammability for prod in products]
    # Return mean values
    print("Mean Price: $", sum(prices) / float(len(prices)))
    print("Mean Weight: $", sum(weights) / float(len(weights)))
    print("Mean Flammability: $", sum(flammabilities) / float(len(flammabilities)))