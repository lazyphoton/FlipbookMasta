### flipbook_core.py
import os
from PIL import Image

def create_flipbook(
    input_folder,
    output_file,
    grid_size=16,
    canvas_size=4096,
    allow_overflow=False
):
    image_files = sorted([
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])
    total_frames = len(image_files)
    max_frames = grid_size * grid_size

    if total_frames > max_frames:
        if not allow_overflow:
            raise ValueError(f"Too many frames: {total_frames}. Max is {max_frames} for {grid_size}x{grid_size} grid.")
        image_files = image_files[:max_frames]  # Clip extra frames

    cell_size = canvas_size // grid_size
    canvas = Image.new('RGBA', (canvas_size, canvas_size), (0, 0, 0, 0))

    for idx, filename in enumerate(image_files):
        img = Image.open(os.path.join(input_folder, filename)).convert('RGBA')
        resized = img.resize((cell_size, cell_size), Image.BILINEAR)
        row = idx // grid_size
        col = idx % grid_size
        x = col * cell_size
        y = row * cell_size
        canvas.paste(resized, (x, y))

    canvas.save(output_file)
    print(f"Saved {len(image_files)} frames into {grid_size}x{grid_size} grid as {output_file}")
