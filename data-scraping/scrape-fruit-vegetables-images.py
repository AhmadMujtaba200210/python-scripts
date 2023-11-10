import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def download_images(query, num_images=10, save_path='images'):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Format the search query
    search_url = f'https://www.google.com/search?q={query}&tbm=isch'

    # Send a request to the Google Images search
    response = requests.get(search_url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and download images
    image_tags = soup.find_all('img')
    for i, img_tag in enumerate(image_tags[:num_images]):
        img_url = img_tag.get('src')
        img_url = urljoin(search_url, img_url)

        # Download the image
        response = requests.get(img_url)
        img_data = response.content

        # Save the image to the specified directory
        img_name = f'{query}_{i + 1}.jpg'
        img_path = os.path.join(save_path, img_name)

        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)

        print(f'Downloaded {img_name}')


if __name__ == '__main__':
    # Replace 'oranges' with your desired search query
    download_images('ground black pepper in bowl', num_images=100)
