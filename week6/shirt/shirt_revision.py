from sys import argv, exit
from PIL import Image, ImageOps
from os.path import splitext


EXTENSIONS = (".jpg", ".jpeg", ".png")


def main():
    #  VALIDATE AND STORE COMMAND-LINE ARGUMENTS
    input_image, output_name = validate_arguments()

    #  RETURNS IF IMAGE FILE EXISTS
    shirt = validate_image("shirt.png")
    muppet = validate_image(input_image)

    result = overlay_images(shirt, muppet)

    result.save(output_name)


def validate_arguments() -> tuple:
    #  VALIDATE 2 COMMAND LINE INPUTS
    if len(argv) != 3:
        exit("Usage: python shirt.py before.png after.png")

    #  ISOLATE .EXTENSIONS
    input_extension: tuple = splitext(argv[1])[1]
    output_extension: tuple = splitext(argv[2])[1]

    #  CHECKS VALID EXTENSION AND IF INPUT & OUTPUT EXTENSIONS MATCH @csfive for reference
    if (
        not input_extension in EXTENSIONS
        or not output_extension in EXTENSIONS
        or input_extension != output_extension
    ):
        exit("Invalid or Missing Arguments")

    else:
        return argv[1], argv[2]


def overlay_images(shirt, muppet):
    #  RESIZE MUPPET IMAGE TO SHIRT IMAGE DIMENSIONS
    result = ImageOps.fit(image=muppet, size=shirt.size)

    #  PASTE MASKED SHIRT IMAGE ON TOP OF MUPPET IMAGE
    result.paste(im=shirt, mask=shirt)
    return result


def validate_image(image_file):
    try:
        image = Image.open(image_file)
        return image

    except FileNotFoundError:
        exit("Image does not exist")


if __name__ == "__main__":
    main()

