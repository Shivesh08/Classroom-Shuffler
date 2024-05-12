import csv
import random
import tkinter as tk
from tkinter import filedialog, messagebox

output_file_path = ""  # Initialize output_file_path globally

def shuffle_sections():
    global output_file_path  # Access the global variable

    # Number of section required
    secn = int(section_entry.get())

    # Read data from the CSV file
    with open(data_file_path, newline='') as f:
        reader = csv.reader(f)
        data = [row[0] for row in reader]

    # Shuffle the data
    random.shuffle(data)

    # Define number of elements in data
    elem = len(data)

    if secn >= elem:
        messagebox.showerror("Error", "The number of sections requested is more than the number of students!")
        return

    # Define chunk size and remainder
    chunk_size = elem // secn
    remainder = elem % secn

    if not output_file_path:
        output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not output_file_path:
            return

    # Open a new CSV file for writing
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Iterate over chunks and write to CSV
        chunk_num = 0
        start = 0
        for section in range(secn):
            extra = 1 if section < remainder else 0
            end = start + chunk_size + extra
            section_data = data[start:end]
            writer.writerow([f'Section {chr(ord("A") + section)}'])
            writer.writerows([[item] for item in section_data])
            writer.writerow([])
            start = end

    messagebox.showinfo("Success", f"{elem} students have been shuffled into {secn} sections.")

def browse_data_file():
    global data_file_path
    data_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if data_file_path:
        data_label.config(text=data_file_path)

def browse_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if output_file_path:
        output_label.config(text=output_file_path)

# Create GUI
root = tk.Tk()
root.title("Classroom Shuffler")

data_file_path = ""

section_label = tk.Label(root, text="Number of Sections:")
section_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
section_entry = tk.Entry(root)
section_entry.grid(row=0, column=1, padx=10, pady=5)

data_button = tk.Button(root, text="Select Data File", command=browse_data_file)
data_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")

data_label = tk.Label(root, text="No file selected")
data_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

output_button = tk.Button(root, text="Browse Output File", command=browse_output_file)
output_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")

output_label = tk.Label(root, text="No file selected")
output_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

shuffle_button = tk.Button(root, text="Shuffle Sections", command=shuffle_sections)
shuffle_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
