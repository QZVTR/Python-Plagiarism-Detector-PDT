import os


def list_files(dir):
    return os.listdir(dir)


def create_file(name, content):
    with open(name, "w") as file:
        file.write(content)


def read_file(name):
    with open(name, "r") as file:
        return file.read()


def delete_file(name):
    os.remove(name)


def rename_file(old_name, new_name):
    os.rename(old_name, new_name)


def copy_file(source, destination):
    # Implement file copying logic
    pass


def move_file(source, destination):
    # Implement file moving logic
    pass


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
