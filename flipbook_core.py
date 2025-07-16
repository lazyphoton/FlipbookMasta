import os
import math
from PIL import Image

def create_flipbook(
    input_folder,
    output_file,
    grid_size=16,
    canvas_size=2048,
    force_square=True
):
    image_files = sorted([
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    total_frames = len(image_files)
    max_per_texture = grid_size * grid_size
    num_textures = math.ceil(total_frames / max_per_texture)
    cell_size = canvas_size // grid_size

    for tex_index in range(num_textures):
        canvas = Image.new('RGBA', (canvas_size, canvas_size), (0, 0, 0, 0))

        start_idx = tex_index * max_per_texture
        end_idx = min(start_idx + max_per_texture, total_frames)
        frame_chunk = image_files[start_idx:end_idx]

        for idx, filename in enumerate(frame_chunk):
            img = Image.open(os.path.join(input_folder, filename)).convert('RGBA')
            if force_square:
                img = img.resize((cell_size, cell_size), Image.BILINEAR)
            else:
                img.thumbnail((cell_size, cell_size), Image.BILINEAR)

            row = idx // grid_size
            col = idx % grid_size
            x = col * cell_size
            y = row * cell_size
            canvas.paste(img, (x, y))

        base, ext = os.path.splitext(output_file)
        indexed_output = f"{base}_{tex_index:02}{ext}"
        canvas.save(indexed_output)
        print(f"Saved {len(frame_chunk)} frames to {indexed_output}")
