import os


# Comment 1
def list_files(directory):
    return os.listdir(directory)


# Comment 2
def create_file(name, content):
    with open(name, "w") as file:
        file.write(content)


# Comment 3
def read_file(name):
    with open(name, "r") as file:
        return file.read()


# Comment 4
def delete_file(name):
    os.remove(name)


# Comment 5
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


# Comment 6
def copy_file(source, destination):
    # Implement file copying logic
    pass


# Comment 7
def move_file(source, destination):
    # Implement file moving logic
    pass


# Comment 8
def get_file_size(name):
    return os.path.getsize(name)


def get_file_extension(name):
    return os.path.splitext(name)[1]


def main():
    # Implement user interface for file management
    files = list_files(".")
    print(files)  # Example usage


if __name__ == "__main__":
    main()
