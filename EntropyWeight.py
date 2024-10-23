import pandas as pd
import numpy as np

# Step 1: Load the data from Excel
file_path = 'data.xlsx'  # Replace with your local Excel file path
data = pd.read_excel(file_path)

# Step 2: Remove the 'Time' column (if present) and focus on X1 to X20
data_for_entropy = data.drop(columns=['Time'])

# Step 3: Normalize the data (if not already normalized, skip this step if it is normalized)
# Assuming the data is already normalized within the range [0, 1]

# Step 4: Calculate entropy for each indicator
n = len(data_for_entropy)  # number of rows
k = 1.0 / np.log(n)  # constant k

# Calculate proportion p_ij for each element in the dataset
p_ij = data_for_entropy.div(data_for_entropy.sum(axis=0), axis=1)

# Calculate the entropy for each column (indicator)
entropy = -k * (p_ij * np.log(p_ij + 1e-12)).sum(axis=0)  # Adding a small constant to avoid log(0)

# Step 5: Calculate the degree of divergence for each indicator
d = 1 - entropy

# Step 6: Calculate the weights (normalized degree of divergence)
weights = d / d.sum()

# Step 7: Convert weights into a DataFrame for easy viewing
weights_df = pd.DataFrame(weights, columns=['Weight'])

# Display the weights
print(weights_df)

# Optionally, save the weights to a new Excel file
output_path = 'entropy_weights.xlsx'  # Replace with your desired output path
weights_df.to_excel(output_path, index=True)

print(f"Entropy weights saved to {output_path}")
