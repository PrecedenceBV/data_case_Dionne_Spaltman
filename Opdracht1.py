import pandas

import pandas as pd

# Define the file path
file_path = '/Users/precedenceintern/PycharmProjects/data_case_Dionne_Spaltman/data-case/customer_data_comma.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Optional: Display the first few rows
print(df.head())