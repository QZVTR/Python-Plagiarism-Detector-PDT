import os


def list_files(dir):
    return os.listdir(dir)


def create_file(a, b):
    with open(a, "w") as file:
        file.write(b)


def read_file(road):
    with open(road, "r") as file:
        return file.read()


def delete_file(stri):
    os.remove(stri)


def rename_file(newName, oldName):
    os.rename(newName, oldName)


def copy_file(x, y):
    # Implement file copying logic
    pass


def move_file(z, j):
    # Implement file moving logic
    pass


def get_file_size(getv):
    return os.path.getsize(getv)


def get_file_extension(n):
    return os.path.splitext(n)[1]


def main():
    # Implement user interface for file management
    files = list_files(".")
    print(files)  # Example usage


if __name__ == "__main__":
    main()
