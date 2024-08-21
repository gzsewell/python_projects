'''
Program takes excel file and CSV file as inputs.
A series of checks take place to determine if the .csv file is valid.
Printing the first few lines of the CSV was more of a troubleshooting step.

The same checks are made for the Excel file.

Combines CSV into one list.
Prints the data in CSV.
Prints the data that will be deleted from the Excel file. 
 
Blah blah some other things and this was harder than I thought. 
'''


import pandas as pd

# Load the CSV file into a DataFrame
try:
    csv_df = pd.read_csv('the_Source.csv', header=None)
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("The CSV file was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("The CSV file is empty.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the CSV file: {e}")
    exit()

# Print the first few rows of the CSV DataFrame for debugging
print("CSV DataFrame Head:\n", csv_df.head())

# Check if the CSV DataFrame is empty
if csv_df.empty:
    print("The CSV file is empty.")
    exit()

# Load the Excel file into a DataFrame
try:
    excel_df = pd.read_excel('excel_test_one.xlsx')
    print("Excel file loaded successfully.")
except FileNotFoundError:
    print("The Excel file was not found.")
    exit()
except pd.errors.EmptyDataError:
    print("The Excel file is empty.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the Excel file: {e}")
    exit()

# Combine all CSV values into a single list
csv_values = csv_df.values.flatten().tolist()

# Print the CSV values for debugging
print("CSV Values:", csv_values)

# Create a DataFrame to store deleted rows
deleted_rows = pd.DataFrame()

# Iterate over each value in the list
for value in csv_values:
    # Print the value being searched for
    print("Searching for:", value)
    # Find the matching rows in the Excel DataFrame
    matching_rows = excel_df[excel_df.apply(lambda row: any(value.strip().lower() in str(cell).strip().lower() for cell in row), axis=1)]
    # Append matching rows to the deleted_rows DataFrame
    deleted_rows = pd.concat([deleted_rows, matching_rows])
    # Drop the matching rows from the Excel DataFrame
    excel_df = excel_df.drop(matching_rows.index)

# Save the modified Excel DataFrame back to the Excel file
excel_df.to_excel('output.xlsx', index=False)

# Print the deleted rows for troubleshooting
print("Deleted Rows:\n", deleted_rows)

print("The contents of the CSV file were successfully deleted from the Excel file and saved as output.xlsx")