import pickle
import pathlib

# 📝 Funktion för att spara textdata till en fil
def save_file(data, filename, filepath):
    """Spara textdata till en fil."""

    print("Saving file...")

    with open(filepath + "/" + filename, 'w') as file:
        file.write(data)

# 📂 Funktion för att läsa textdata från en fil
def load_file(filename, filepath):
    """Läs och returnera textdata från en fil."""

    print("Loading file...")

    with open(str(pathlib.Path.cwd()) + filepath + "/" + filename, 'r') as file:
        return file.read()

# 💾 Funktion för att spara binärdata med pickle
def save_bin_file(data, filename, filepath):
    """Spara binärdata med pickle."""

    print("Saving binary file...")

    with open(str(pathlib.Path.cwd()) + filepath + "/" + filename, 'wb') as file:
        pickle.dump(data, file)

# 📦 Funktion för att läsa binärdata med pickle
def load_bin_file(filename, filepath):
    """Läs och returnera binärdata med pickle."""

    print("Attempting to load bin file...")

    try:
        with open(str(pathlib.Path.cwd()) + filepath + "/" + filename, 'rb') as file:
            print("Binary file found...")
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("No file found...")
        return {}  # Returnera en tom ordbok om filen inte finns eller är tom
