from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import requests


def download_images(query, num_images=30, save_path='images'):
    # Create the save directory if it doesn't exist
    save_path = save_path + "/" + query
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Create a new instance of the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Format the search query
        search_url = f'https://www.bing.com/images/search?q={query}'

        # Open the Bing Images page
        driver.get(search_url)

        # Scroll down to load more images using JavaScript
        for _ in range(num_images // 20):
            driver.find_element(By.XPATH, '//body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)

        # Get the updated page source after scrolling
        updated_page_source = driver.page_source

        # Parse the HTML content of the updated page
        image_tags = driver.find_elements(By.XPATH, '//img[@class="mimg"]')
        for i, img_tag in enumerate(image_tags[:num_images]):
            img_url = img_tag.get_attribute('src')

            # Skip if the image URL is empty
            if not img_url:
                continue

            # Save the image to the specified directory
            img_name = f'{query}_{i + 1}.jpg'
            img_path = os.path.join(save_path, img_name)

            # Use requests to download the image
            response = requests.get(img_url)
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)

            print(f'Downloaded {img_name}')

    finally:
        # Close the webdriver
        driver.quit()


if __name__ == '__main__':
    # Replace 'apple fruit' with your desired search query
    download_images('ginger', num_images=200)
