# Specify the path to your text file
input_text_file = 'cleaned.txt'

# Specify the output text file name (change it according to your preference)
output_text_file = 'cleaned.txt'

# Open the input text file for reading
with open(input_text_file, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Clean each line by replacing colons and dashes with spaces
cleaned_lines = [line.replace(':', ' ').replace('-', ' ').replace('"','').replace(' I ', '').replace(' II ', '').replace('!','') for line in lines]

# Open the output text file for writing
with open(output_text_file, 'w') as file:
    # Write the cleaned lines to the output file
    file.writelines(cleaned_lines)

print(f'The text file has been cleaned and saved as {output_text_file}.')
