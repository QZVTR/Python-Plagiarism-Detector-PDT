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
    xCopy = x[:]
    yCopy = y[:]
    return xCopy, yCopy


def move_file(z, j):
    # Implement file moving logic
    z, j = j, z
    return z, j


def getFileSize(name):
    return os.path.getsize(name)


def getFileExtension(name):
    return os.path.splitext(name)[1]


def main():
    # Implement user interface for file management
    files = list_files(".")
    print(getFileSize(files[0]))
    print(files)  # Example usage


if __name__ == "__main__":
    main()
