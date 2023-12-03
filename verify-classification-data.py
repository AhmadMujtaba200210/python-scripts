import os
import pandas as pd
import requests

# Directory containing the images
image_directory = "/Users/Container/python_workspace/python-scripts/images/"

# API endpoint
api_endpoint = "http://localhost:82/predict"

# Initialize an empty DataFrame
result_df = pd.DataFrame(columns=["ImageName", "item1", "item2", "item3", "item4", "item5"])

# Iterate through each file in the directory
for file_name in os.listdir(image_directory):
    # Check if the file is an image (JPEG or PNG)
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Full path to the image
        image_path = os.path.join(image_directory, file_name)

        # Open the image file in binary mode
        with open(image_path, 'rb') as image_file:
            # Prepare the files parameter with the image
            files = {'file': ('image.jpg', image_file, 'image/jpeg')}

            # Make a POST request to the API
            response = requests.post(api_endpoint, files=files)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            api_response = response.json()

            # Extracting data from the API response
            labels = list(api_response["result"].keys())
            scores = list(api_response["result"].values())

            # Extract the base name without extension
            image_name = os.path.splitext(file_name)[0]

            # Creating a row for the DataFrame
            row = {
                "ImageName": image_name,
                "item1": f"{labels[0]}:{scores[0]}",
                "item2": f"{labels[1]}:{scores[1]}",
                "item3": f"{labels[2]}:{scores[2]}",
                "item4": f"{labels[3]}:{scores[3]}",
                "item5": f"{labels[4]}:{scores[4]}",
            }

            # Append the row to the DataFrame
            result_df = result_df._append(row, ignore_index=True)
        else:
            print(f"Error for image '{file_name}': {response.status_code} - {response.text}")

# Save the DataFrame to a CSV file
csv_filename = "output_results.csv"
result_df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' has been created.")
