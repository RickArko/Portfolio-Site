from PIL import Image
from pathlib import Path


PATH = Path("src").joinpath("static", "images", "ra-pit.ico")

if __name__ == "__main__":

    if PATH.exists():

        # Open the image file
        image = Image.open(PATH)

        # Resize the image to 16x16 pixels
        favicon = image.resize((16, 16))
        favicon = image.resize((32, 32))

        # Save the resized image as an ICO file
        NEWPATH = Path("src").joinpath("static", "favicon.ico")
        favicon.save(NEWPATH, format='ICO')
