import pandas as pd
import numpy as np

# Load the dataset (replace with the correct path for your file)
data = pd.read_excel('data/dataLNormalized.xlsx')

# Step 1: Normalize the data (assuming the data is already normalized)

# Step 2: Calculate entropy for each indicator
def calculate_entropy(data):
    # Avoid division by zero
    data = data + 1e-12
    P = data / data.sum(axis=0)  # Calculate proportion
    entropy = -np.sum(P * np.log(P), axis=0) / np.log(len(data))  # Calculate entropy
    return entropy

# Step 3: Calculate the entropy weight for each indicator
def entropy_weight_method(data):
    entropy = calculate_entropy(data)
    d = 1 - entropy  # Calculate diversity
    weights = d / d.sum()  # Calculate weights
    return weights

# Step 4: Apply entropy weight method for each region
grouped_data = data.groupby('Location')
weights_by_region = grouped_data.apply(lambda group: entropy_weight_method(group[['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']]))
weights_by_region.to_excel('data/entropy_weights_by_region.xlsx')
# Display the weights for each region
print(weights_by_region)
