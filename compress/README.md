# PDF Compressor

A simple GUI tool to compress PDF files using Ghostscript.

## Requirements

- Python 3 with tkinter
- [Ghostscript](https://ghostscript.com/)

## Setup

### macOS

```bash
brew install python-tk ghostscript
```

### Linux

**Debian / Ubuntu**

```bash
sudo apt install python3-tk ghostscript
```

**Fedora**

```bash
sudo dnf install python3-tkinter ghostscript
```

**Arch**

```bash
sudo pacman -S tk ghostscript
```

### Windows

1. Install [Python 3](https://www.python.org/downloads/) (enable "Add Python to PATH" during setup; tkinter is included by default).
2. Install Ghostscript:

```powershell
winget install Artifex.Ghostscript
```

Or download the installer from [ghostscript.com/releases](https://ghostscript.com/releases/gsdnld.html).

After installing Ghostscript, restart your terminal so `gswin64c` is on your PATH.

## Usage

**macOS / Linux**

```bash
python3 pdf_compressor.py
```

**Windows**

```powershell
python pdf_compressor.py
```

Select a compression level, pick a PDF, and choose where to save the compressed file.
