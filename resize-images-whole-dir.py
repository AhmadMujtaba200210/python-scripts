from PIL import Image
import os


def resize_images(directory, output_size=(256, 256)):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Open the image file
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)

            # Resize the image
            resized_img = img.resize(output_size)

            # Save the resized image, overwriting the original
            resized_img.save(img_path)
            print(f'Resized {filename} to {output_size}')


if __name__ == '__main__':
    # Replace 'your_directory' with the path to your image directory
    image_directory = '/Users/Container/python_workspace/python-scripts/images'

    resize_images(image_directory)
