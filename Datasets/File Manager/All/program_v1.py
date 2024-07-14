import os


def main():
    # Implement user interface for file management
    files = list_files(".")
    print(files)  # Example usage


def get_file_extension(name):
    return os.path.splitext(name)[1]


# Comment 1


def create_file(name, content):
    with open(name, "w") as file:
        file.write(content)


# Comment 1
def read_file(number):
    with open(number, "r") as file:
        return file.read()


def get_file_size(name):
    return os.path.getsize(name)


def delete_file(name):
    os.remove(name)


def move_file(source, destination):
    # Implement file moving logic
    pass  # Comment 1


def rename_file(old, new):
    os.rename(old, new)


def copy_file(source, destination):
    # Implement file copying logic
    pass


def list_files(directory):
    return os.listdir(directory)


# Comment 1

if __name__ == "__main__":
    main()
