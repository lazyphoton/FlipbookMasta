# 🎞️ FlipbookMasta

**FlipbookMasta** is a Python-based tool for generating optimized texture atlases (a.k.a. flipbook textures) for use in Unreal Engine 5, game engines, or animation tools.

It automatically:
- Loads a folder of same-size image frames
- Resizes and arranges them into a defined grid layout (e.g., `4x8`, `8x16`)
- Outputs one or more PNG atlases with clean naming (e.g. `T_JumpScare_4x8_00.png`)

---

## ✅ Features

- Supports any number of frames — creates multiple atlases as needed  
- Preserves aspect ratio of selected grid (no forced square unless defined)  
- Clean, readable filenames like `T_Explosion_8x8.png`, `T_Flames_4x8_02.png`  
- GUI (Tkinter) and CLI support coming soon  
- Production-ready for UEFN, UE5, or other tools  

---

## 🧩 Example Usage

```python
from flipbook_core import create_flipbook

create_flipbook(
    input_folder="input_frames",
    output_file="T_MyFlipbook.png",
    grid_cols=4,
    grid_rows=8,
    canvas_size=2048
)
```

---

## 🖥️ Creating a Standalone `.exe`

To share FlipbookMasta as a Windows `.exe` (no Python install needed):

### 1. Set up a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install required libraries

```bash
pip install pillow pyinstaller
```

### 3. Build the `.exe`

From the root folder (where `flipbook_gui.py` is located), run:

```bash
pyinstaller --noconfirm --onefile --windowed flipbook_gui.py
```

This creates a standalone `.exe` in the `dist/` folder.

> 💡 `--windowed` prevents a terminal window from opening.

---

## 📁 Output Format

Filenames include grid layout and auto-numbering when needed:

- `T_Explosion_4x8.png` — if only one atlas
- `T_Explosion_4x8_00.png`, `T_Explosion_4x8_01.png` — if multiple atlases are needed

---

## 📦 Dependencies

- Python 3.8 or later
- [Pillow](https://pillow.readthedocs.io/)

