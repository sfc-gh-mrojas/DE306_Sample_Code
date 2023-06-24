import os

def check_file_exists(file_path):
    """
    Checks if a file exists at the specified path.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path)

def create_directory(directory_path):
    """
    Creates a directory at the specified path if it doesn't already exist.

    Args:
        directory_path (str): The path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

if __name__ == "__main__":
    # Sample usage of utils functions
    file_path = "/path/to/file.txt"

    # Check if the file exists
    file_exists = check_file_exists(file_path)
    print(f"File exists: {file_exists}")

    # Create a directory
    directory_path = "/path/to/directory"
    create_directory(directory_path)
    print("Directory created")

