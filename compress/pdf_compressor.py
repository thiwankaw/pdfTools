import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

def compress_pdf(input_file_path, output_file_path, power_level):
    """Compresses the PDF using Ghostscript."""
    quality_levels = {
        "Default": '/default',
        "Prepress (High)": '/prepress',
        "Printer (Medium-High)": '/printer',
        "Ebook (Medium)": '/ebook',
        "Screen (Smallest Size)": '/screen'
    }

    gs_command = [
        "gs", 
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={quality_levels.get(power_level, '/screen')}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_file_path}",
        input_file_path
    ]

    try:
        subprocess.run(gs_command, check=True)
        
        # Calculate compression stats
        original_size = os.path.getsize(input_file_path) / (1024 * 1024)
        new_size = os.path.getsize(output_file_path) / (1024 * 1024)
        
        return True, original_size, new_size
    except subprocess.CalledProcessError as e:
        return False, str(e), 0
    except Exception as e:
        return False, str(e), 0

def select_and_compress():
    # Open file picker
    input_path = filedialog.askopenfilename(
        title="Select a PDF to compress",
        filetypes=[("PDF Files", "*.pdf")]
    )
    
    if not input_path:
        return # User cancelled

    # Ask where to save
    output_path = filedialog.asksaveasfilename(
        title="Save compressed PDF as...",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        initialfile="compressed_output.pdf"
    )

    if not output_path:
        return # User cancelled

    # Get the selected compression level
    level = compression_var.get()
    
    # Run compression
    success, orig_size, new_size = compress_pdf(input_path, output_path, level)
    
    if success:
        messagebox.showinfo(
            "Success!", 
            f"PDF Compressed successfully!\n\n"
            f"Original: {orig_size:.2f} MB\n"
            f"New: {new_size:.2f} MB\n"
            f"Saved: {(orig_size - new_size):.2f} MB"
        )
    else:
        messagebox.showerror("Error", f"Failed to compress:\n{orig_size}")

# --- Build the GUI ---
root = tk.Tk()
root.title("Local PDF Compressor")
root.geometry("350x200")
root.eval('tk::PlaceWindow . center') # Center on screen

tk.Label(root, text="Select Compression Level:", font=("Arial", 14)).pack(pady=(20, 5))

compression_var = tk.StringVar(value="Screen (Smallest Size)")
levels = ["Screen (Smallest Size)", "Ebook (Medium)", "Printer (Medium-High)", "Prepress (High)", "Default"]
dropdown = ttk.Combobox(root, textvariable=compression_var, values=levels, state="readonly", width=25)
dropdown.pack(pady=5)

compress_btn = tk.Button(root, text="Select PDF & Compress", command=select_and_compress, height=2)
compress_btn.pack(pady=20)

root.mainloop()

