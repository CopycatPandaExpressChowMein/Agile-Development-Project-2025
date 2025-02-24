import pickle
import pathlib

# 📝 Funktion för att spara textdata till en fil
def save_file(data, filename, filepath=str(pathlib.Path.cwd())):
    """Spara textdata till en fil."""
    with open(filepath + "/" + filename, 'w') as file:
        file.write(data)

# 📂 Funktion för att läsa textdata från en fil
def load_file(filename, filepath=str(pathlib.Path.cwd())):
    """Läs och returnera textdata från en fil."""
    with open(filepath + "/" + filename, 'r') as file:
        return file.read()

# 💾 Funktion för att spara binärdata med pickle
def save_bin_file(data, filename, filepath=str(pathlib.Path.cwd())):
    """Spara binärdata med pickle."""
    with open(filepath + "/" + filename, 'wb') as file:
        pickle.dump(data, file)

# 📦 Funktion för att läsa binärdata med pickle
def load_bin_file(filename, filepath=str(pathlib.Path.cwd())):
    """Läs och returnera binärdata med pickle."""
    try:
        with open(filepath + "/" + filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}  # Returnera en tom ordbok om filen inte finns eller är tom
