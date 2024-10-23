import pandas as pd

# Load the data (replace with the correct paths to your files)
dataLT = pd.read_excel('data/dataLT.xlsx')
weightL = pd.read_excel('data/WeightL.xlsx')
# Remove conflicting columns from weightL if they exist in dataLT (e.g., 'X1' to 'X7')
weightL = weightL.drop(columns=['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'], errors='ignore')

# Merge the two DataFrames without suffixes
merged_data = pd.merge(dataLT, weightL, on='Location', suffixes=('', ''))
# Assuming both files have a common column like 'Location' to join on
# Modify the column names if needed
# merged_data = pd.merge(dataLT, weightL, on='Location')
print(merged_data)
# Multiply each of the indicators (e.g., 'X1' to 'X7') by their corresponding weights
# Assuming dataLT has columns 'X1', 'X2', ..., 'X7' and WeightL has 'Weight_X1', 'Weight_X2', ..., 'Weight_X7'
merged_data['s'] = (
    merged_data['X1'] * merged_data['Weight_X1'] +
    merged_data['X2'] * merged_data['Weight_X2'] +
    merged_data['X3'] * merged_data['Weight_X3'] +
    merged_data['X4'] * merged_data['Weight_X4'] +
    merged_data['X5'] * merged_data['Weight_X5'] +
    merged_data['X6'] * merged_data['Weight_X6'] +
    merged_data['X7'] * merged_data['Weight_X7']
)

# Save the updated data with the new 's' column to an Excel file
merged_data.to_excel('data/dataLT_with_s.xlsx', index=False)

print("New data with 's' column has been saved to 'dataLT_with_s.xlsx'.")
