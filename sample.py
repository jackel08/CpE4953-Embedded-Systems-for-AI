#pip install fcsparser pandas


from fcsparser import parse
import pandas as pd
import matplotlib.pyplot as plt

# Path to the .fcs file
fcs_file = "bob.fcs"

# Parse the .fcs file
metadata, data = parse(fcs_file, reformat_meta=True)

# Print the actual column names to identify the correct ones
print(data.columns) 

# Scatter plot of two fluorescence channels
plt.figure(figsize=(8, 6))
# Assuming 'FSC-A' and 'SSC-A' are present in data.columns:
try:
    plt.scatter(data['FSC-A'], data['SSC-A'], alpha=0.5, s=1, c='blue')  
except KeyError:
    # If 'FSC-A' or 'SSC-A' are not found, use index-based access 
    # Replace 0 and 1 with the actual column indices from data.columns
    plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha=0.5, s=1, c='blue')  
    print("Warning: Using index-based access for scatter plot. Verify column indices.")
plt.title('Scatter Plot: FSC-A vs SSC-A')
plt.xlabel('FSC-A (Forward Scatter)')
plt.ylabel('SSC-A (Side Scatter)')
plt.show()

# Histogram of a single channel
plt.figure(figsize=(8, 6))
try:
    plt.hist(data['FSC-A'], bins=100, color='green', alpha=0.7) 
except KeyError:
    # If 'FSC-A' is not found, use index-based access
    # Replace 0 with the actual column index from data.columns
    plt.hist(data.iloc[:, 0], bins=100, color='green', alpha=0.7)  
    print("Warning: Using index-based access for histogram. Verify column index.")
plt.title('Histogram: FSC-A')
plt.xlabel('FSC-A (Forward Scatter)')
plt.ylabel('Frequency')
plt.show()