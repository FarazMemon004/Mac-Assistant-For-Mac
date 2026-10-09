import os

def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Example usage:
create_folder('/Users/apple/Desktop/NewFolder')
delete_file('/Users/apple/Desktop/old_file.txt')
