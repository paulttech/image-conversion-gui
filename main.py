import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_image_to_jpeg(input_image_path, output_folder):
    try:
        # Open the image
        with Image.open(input_image_path) as img:
            # Convert to RGB mode (required for JPEG)
            rgb_img = img.convert('RGB')
            # Extract filename without extension
            filename = os.path.splitext(os.path.basename(input_image_path))[0]
            # Save as JPEG in the specified output folder
            output_image_path = os.path.join(output_folder, filename + '.jpg')
            rgb_img.save(output_image_path, 'JPEG')
            print("Image converted to JPEG and saved successfully.")
            return True
    except Exception as e:
        print(f"Error converting image: {e}")
        return False

def browse_file():
    filepath = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filepath)

def browse_folder():
    folderpath = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folderpath)

def convert_image():
    input_image_path = entry_file.get()
    output_folder = entry_folder.get()
    convert_image_to_jpeg(input_image_path, output_folder)

# Create the main application window
root = tk.Tk()
root.title("Image Converter - Any to JPEG")

# Create and pack widgets
label_file = tk.Label(root, text="Input Image:")
label_file.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry_file = tk.Entry(root, width=40)
entry_file.grid(row=0, column=1, padx=5, pady=5)

button_browse_file = tk.Button(root, text="Browse", command=browse_file)
button_browse_file.grid(row=0, column=2, padx=5, pady=5)

label_folder = tk.Label(root, text="Output Folder:")
label_folder.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry_folder = tk.Entry(root, width=40)
entry_folder.grid(row=1, column=1, padx=5, pady=5)

button_browse_folder = tk.Button(root, text="Browse", command=browse_folder)
button_browse_folder.grid(row=1, column=2, padx=5, pady=5)

button_convert = tk.Button(root, text="Convert", command=convert_image)
button_convert.grid(row=2, column=1, pady=10)

# Run the main event loop
root.mainloop()
