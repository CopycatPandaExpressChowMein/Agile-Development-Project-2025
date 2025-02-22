import pickle
import pathlib


def save_file(data, filename, filepath=pathlib.Path.cwd().__str__()):
    with open(filepath + "/" + filename, 'w') as file:
        file.write(data)


def load_file(filename, filepath=pathlib.Path.cwd().__str__()):
    with open(filepath + "/" + filename, 'r') as file:
        return file.read()


def save_bin_file(data, filename, filepath=pathlib.Path.cwd().__str__()):
    with open(filepath + "/" + filename, 'wb') as file:
        pickle.dump(data, file)


def load_bin_file(filename, filepath=pathlib.Path.cwd().__str__()):
    with open(filepath + "/" + filename, 'rb') as file:
        return pickle.load(file)

