import pickle




def save_file(data, filepath, filename):
    with open(filepath + "/" + filename, 'w') as file:
        file.write(data)


def load_file(data, filepath, filename):
    with open(filepath + "/" + filename, 'r') as file:
        file.read(data)


def save_bin_file(data, filepath, filename):
    with open(filepath + "/" + filename, 'wb') as file:
        pickle.dump(data, file)


def load_bin_file(data, filepath, filename):
    with open(filepath + "/" + filename, 'rb') as file:
        pickle.load(data, file)

