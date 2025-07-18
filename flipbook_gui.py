### flipbook_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from flipbook_core import create_flipbook

def browse_input():
    path = filedialog.askdirectory()
    if path:
        input_path.set(path)

def browse_output():
    path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if path:
        output_path.set(path)

def run_flipbook():
    try:
        grid_str = grid_config_var.get()
        cols, rows = map(int, grid_str.split('x'))

        create_flipbook(
            input_folder=input_path.get(),
            output_file=output_path.get(),
            grid_cols=cols,
            grid_rows=rows,
            canvas_size=int(resolution_var.get()),
        )
        messagebox.showinfo("Success", "Flipbook created successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("FlipbookMasta")

input_path = tk.StringVar()
output_path = tk.StringVar()
grid_config_var = tk.StringVar(value="16x16")
resolution_var = tk.StringVar(value="4096")

ttk.Label(root, text="Input Folder:").grid(row=0, column=0, sticky="e")
ttk.Entry(root, textvariable=input_path, width=40).grid(row=0, column=1)
ttk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2)

ttk.Label(root, text="Output File:").grid(row=1, column=0, sticky="e")
ttk.Entry(root, textvariable=output_path, width=40).grid(row=1, column=1)
ttk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

ttk.Label(root, text="Grid Layout:").grid(row=2, column=0, sticky="e")
ttk.Combobox(root, textvariable=grid_config_var, values=["2x2", "2x4", "4x4", "4x8", "8x8", "8x16", "16x16"]).grid(row=2, column=1, sticky="w")

ttk.Label(root, text="Canvas Resolution:").grid(row=3, column=0, sticky="e")
ttk.Combobox(root, textvariable=resolution_var, values=["1024", "2048", "4096"]).grid(row=3, column=1, sticky="w")

ttk.Button(root, text="Create Flipbook", command=run_flipbook).grid(row=4, column=1, pady=10)

root.mainloop()
