import pandas as pd

# Assuming your CSV file is named 'your_data.csv'
csv_file_path = '/Users/Container/java_workspace/FYP/recipe-app/src/main/resources/data/Recipes_Dataset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Extract the 'title' column
title_column = df['title']

# Specify the output text file name (change it according to your preference)
output_text_file = 'titles.txt'

# Export the 'title' column to a text file
title_column.to_csv(output_text_file, index=False, header=False)

print(f'The "title" column has been extracted and exported to {output_text_file}.')

