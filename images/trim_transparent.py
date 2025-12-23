from PIL import Image

def remove_transparent_margins(input_path, output_path=None):
    img = Image.open(input_path).convert("RGBA")

    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()

    if bbox is None:
        raise ValueError("Image is fully transparent.")

    cropped = img.crop(bbox)

    # Overwrite original file if output_path is not provided
    if output_path is None:
        output_path = input_path

    cropped.save(output_path)

if __name__ == "__main__":
    input_image = "false_positive_video.png"      # path to your image
    output_image = "output.png"    # optional; can be same as input

    remove_transparent_margins(input_image, output_image)
