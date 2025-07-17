import os
import math
from PIL import Image

def create_flipbook(
    input_folder,
    output_file,
    grid_cols=16,
    grid_rows=16,
    canvas_size=4096
):
    image_files = sorted([
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    total_frames = len(image_files)
    max_per_texture = grid_cols * grid_rows
    num_textures = math.ceil(total_frames / max_per_texture)

    cell_width = canvas_size // grid_cols
    cell_height = canvas_size // grid_rows

    base_name, ext = os.path.splitext(output_file)
    layout_suffix = f"_{grid_cols}x{grid_rows}"

    for tex_index in range(num_textures):
        canvas = Image.new('RGBA', (canvas_size, canvas_size), (0, 0, 0, 0))

        start_idx = tex_index * max_per_texture
        end_idx = min(start_idx + max_per_texture, total_frames)
        frame_chunk = image_files[start_idx:end_idx]

        for idx, filename in enumerate(frame_chunk):
            img = Image.open(os.path.join(input_folder, filename)).convert('RGBA')
            img = img.resize((cell_width, cell_height), Image.BILINEAR)

            row = idx // grid_cols
            col = idx % grid_cols
            x = col * cell_width
            y = row * cell_height
            canvas.paste(img, (x, y))

        if num_textures == 1:
            final_name = f"{base_name}{layout_suffix}{ext}"
        else:
            final_name = f"{base_name}{layout_suffix}_{tex_index:02}{ext}"

        canvas.save(final_name)
        print(f"Saved {len(frame_chunk)} frames to {final_name}")
