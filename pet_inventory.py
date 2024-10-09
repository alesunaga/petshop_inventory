# Import necessary libraries
import codecademylib3
import pandas as pd

# Load the inventory data from a CSV file
inventory = pd.read_csv('inventory.csv')

# Select the first 10 rows of the inventory data specific to Staten Island
# This will give us an initial glimpse into the data for that location
state_island = inventory.head(10)

# Display product descriptions for Staten Island
product_request = state_island['product_description']

# Filter data for products that are 'seeds' and located in 'Brooklyn'
# This gives us a subset of the inventory for a specific product type and location
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# Add a new column 'in_stock' to the inventory DataFrame
# This column indicates whether the product is in stock (True if quantity > 0, otherwise False)
inventory['in_stock'] = inventory.apply(lambda row: True if row['quantity'] > 0 else False, axis=1)

# Add a new column 'total_value' that calculates the total value of each item in stock
# This is done by multiplying the quantity of each item by its price
inventory['total_value'] = inventory.apply(lambda row: row['price'] * row['quantity'], axis=1)

# Create a lambda function to combine product type and product description into one string
combine_lambda = lambda row: '{} - {}'.format(row['product_type'], row['product_description'])

# Apply the lambda function to each row in the DataFrame to create the 'full_description' column
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

# Display the first 10 rows of the updated inventory DataFrame to verify the changes
print(inventory.head(10))
