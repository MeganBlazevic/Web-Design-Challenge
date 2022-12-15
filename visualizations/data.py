# Add dependencies
import pandas as pd

# Read in the csv file
df = pd.read_csv('../Resources/cities.csv')

# Save the file
df.to_html('data.html', index=False)

# Assign to string
table = df.to_html()

# Print table
print(table)