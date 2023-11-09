from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import base64


def download_images(query, num_images=30, save_path='images'):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Create a new instance of the Chrome webdriver
    driver = webdriver.Chrome()

    try:
        # Format the search query
        search_url = f'https://www.google.com/search?q={query}&tbm=isch'

        # Open the Google Images page
        driver.get(search_url)

        # Scroll down to load more images using JavaScript
        for _ in range(num_images // 10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        # Get the updated page source after scrolling
        updated_page_source = driver.page_source

        # Parse the HTML content of the updated page
        image_tags = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
        for i, img_tag in enumerate(image_tags[:num_images]):
            img_url = img_tag.get_attribute('src')

            # Skip if the image URL is empty or a base64-encoded image
            if not img_url or img_url.startswith('data:image'):
                continue

            # Save the image to the specified directory
            img_name = f'{query}_{i + 1}.jpg'
            img_path = os.path.join(save_path, img_name)

            # Get the image data using Selenium
            img_data = img_tag.screenshot_as_base64

            # Decode base64 and save the image
            img_binary = base64.b64decode(img_data)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_binary)

            print(f'Downloaded {img_name}')

    finally:
        # Close the webdriver
        driver.quit()


if __name__ == '__main__':
    # Replace 'apple' with your desired search query
    download_images('apple fruit', num_images=100)
