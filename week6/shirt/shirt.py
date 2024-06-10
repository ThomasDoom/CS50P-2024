from sys import argv, exit
from PIL import Image, ImageOps
from os.path import splitext


EXTENSIONS = [".jpg", ".jpeg", ".png"]


def main():
    #  VALIDATE AND STORE COMMAND-LINE ARGUMENTS
    input_image, output_image = validate_arguments()

    #  GET MUPPET IMAGE
    muppet = validate_image(input_image)

    #  GET SHIRT IMAGE AND SIZE
    shirt = validate_image("shirt.png")
    size = shirt.size

    #  RESIZE MUPPET IMAGE TO SHIRT.PNG DIMENSIONS
    muppet = ImageOps.fit(muppet, size)

    #  PASTE SHIRT OVER MUPPET
    muppet.paste(shirt, shirt)

    #  SAVE RESULT
    muppet.save(output_image)


def validate_arguments() -> tuple:
    #  VALIDATE 2 COMMAND LINE INPUTS
    if len(argv) != 3:
        exit("Usage: python shirt.py before.png after.png")

    #  SPLIT TO ISOLATE EXTENSION
    try:
        input_split: tuple = splitext(argv[1])
        output_split: tuple = splitext(argv[2])

        #  CHECK FOR VALID EXTENSION TYPES
        validate_extension(input_split)
        validate_extension(output_split)

        if not input_split[1] == output_split[1]:
            raise Exception

    except:
        exit(f"Invalid or Missing Extension")

    return argv[1], argv[2]


def validate_extension(arg) -> bool:
    if arg[1] not in EXTENSIONS:
        raise Exception


def validate_image(image_file):
    try:
        image = Image.open(image_file)
        return image

    except FileNotFoundError:
        exit("Image does not exist")


if __name__ == "__main__":
    main()

