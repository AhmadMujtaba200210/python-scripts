import os


def rename_files(directory_path):
    # Check if there are subdirectories
    if not any(os.path.isdir(os.path.join(directory_path, d)) for d in os.listdir(directory_path)):
        print("No subdirectories found. Renaming files in the main directory only.")

        # Rename files in the main directory
        for file_name in os.listdir(directory_path):
            original_path = os.path.join(directory_path, file_name)
            base_name, extension = os.path.splitext(file_name)
            new_name = base_name.split('_', 1)[0] + extension
            new_path = os.path.join(directory_path, new_name)
            os.rename(original_path, new_path)
    else:
        # Traverse through the directory
        for root, dirs, files in os.walk(directory_path):
            # Rename directories
            for dir_name in dirs:
                original_path = os.path.join(root, dir_name)
                new_name = dir_name.split('_', 1)[0]
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)

            # Rename files
            for file_name in files:
                original_path = os.path.join(root, file_name)
                base_name, extension = os.path.splitext(file_name)
                new_name = base_name.split('_', 1)[0] + extension
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)


if __name__ == "__main__":
    directory_path = "/Users/Container/python_workspace/python-scripts/images"  # Change this to your actual directory path
    rename_files(directory_path)
    print("File and directory names have been modified successfully.")
