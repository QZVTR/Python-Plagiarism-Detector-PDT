import os


def read_file(rod):
    with open(rod, "r") as fileExt:
        return fileExt.read()


def delete_file(stri):
    os.remove(stri)  # Comments


def list_files(dr):
    return os.listdir(dr)


def create_file(xsaf, rgwrg):
    with open(xsaf, "w") as le:
        le.write(rgwrg)


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


"""
Test
Multi-line
"""


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
