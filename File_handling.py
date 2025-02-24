import pickle
import pathlib

# 📝 Funktion för att spara textdata till en fil
def save_file(data, filename, filepath=str(pathlib.Path.cwd())):
    """Spara textdata till en fil."""
    with open(filepath + "/" + filename, 'w') as file:
        file.write(data)

<<<<<<< HEAD

def load_file(filename, filepath=pathlib.Path.cwd().__str__()):
=======
# 📂 Funktion för att läsa textdata från en fil
def load_file(filename, filepath=str(pathlib.Path.cwd())):
    """Läs och returnera textdata från en fil."""
>>>>>>> 776c5ca50f3aaf0cec5a04803ef076d88c37e0e4
    with open(filepath + "/" + filename, 'r') as file:
        return file.read()

# 💾 Funktion för att spara binärdata med pickle
def save_bin_file(data, filename, filepath=str(pathlib.Path.cwd())):
    """Spara binärdata med pickle."""
    with open(filepath + "/" + filename, 'wb') as file:
        pickle.dump(data, file)

<<<<<<< HEAD

def load_bin_file(filename, filepath=pathlib.Path.cwd().__str__()):
    with open(filepath + "/" + filename, 'rb') as file:
        return pickle.load(file)

=======
# 📦 Funktion för att läsa binärdata med pickle
def load_bin_file(filename, filepath=str(pathlib.Path.cwd())):
    """Läs och returnera binärdata med pickle."""
    try:
        with open(filepath + "/" + filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}  # Returnera en tom ordbok om filen inte finns eller är tom
>>>>>>> 776c5ca50f3aaf0cec5a04803ef076d88c37e0e4
