import re

# Specify the path to your final cleaned text file
input_text_file = 'cleaned.txt'

# Specify the output text file name (change it according to your preference)
output_text_file = 'final_text_without_roman.txt'

# Open the final cleaned text file for reading
with open(input_text_file, 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Define a regular expression pattern to match Roman numerals
roman_numerals_pattern = re.compile(r'\b(?:I{1,3}|IV|V|IX|X{1,3}|XL|L|XC|C{1,3}|CD|D|CM|M{1,3}|VI)\b')

# Remove Roman numerals from each line
final_text_without_roman = [roman_numerals_pattern.sub('', line) for line in lines]

# Open the output text file for writing
with open(output_text_file, 'w') as file:
    # Write the final text without Roman numerals to the output file
    file.writelines(final_text_without_roman)

print(f'The text file has been further cleaned by removing Roman numerals. The result is saved as {output_text_file}.')
