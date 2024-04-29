from PIL import Image

def convert_to_grayscale(img, output_path):
    with Image.open(img) as image:
        grayscale_image = image.convert("L")
        grayscale_image.save(output_path)
        print("Saved grayscale image to", output_path)

convert_to_grayscale("C:/Users/inesl/OneDrive/Bureau/ETH 12/Thesis/offroad_map/heightmap1.png", "heightmap1_gray.png")
convert_to_grayscale("C:/Users/inesl/OneDrive/Bureau/ETH 12/Thesis/offroad_map/heightmap2.png", "heightmap2_gray.png")