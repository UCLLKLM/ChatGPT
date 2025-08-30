# ...existing code...
import os

def select_pictures(directory='.', extensions=None):
    if extensions is None:
        extensions = ['.jpg', '.jpeg']
    try:
        entries = os.listdir(directory)
    except FileNotFoundError:
        return []
    pictures = [f for f in entries if any(f.lower().endswith(ext) for ext in extensions)]
    return sorted(pictures)

if __name__ == "__main__":
    folder = input("Enter the directory path (tryk Enter for current dir): ").strip() or '.'
    pics = select_pictures(folder)
    if not pics:
        print("Ingen JPG-filer fundet.")
    else:
        print("JPG-filer fundet:")
        for pic in pics:
            print(pic)
# ...existing code...