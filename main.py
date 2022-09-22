from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resizing(image):
    width, height = image.size
    newHeight = 100 * height / float(width)/1.65
    resizedImage = image.resize((100, int(newHeight)))
    return resizedImage

def grayscaling(image):
    grayscaledImage = image.convert('L')
    return grayscaledImage

def asciiConvertion(image):
    pixelsValues = list(image.getdata())
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixelsValues])
    pixelsCount = len(characters)
    asciiImage = "\n".join([characters[index:(index + 100)] for index in range(0, pixelsCount, 100)])
    return asciiImage

def main():
    print('type image path:')
    imagePath = input()

    try: Image.open(imagePath)
    except: print('invalide image path')

    with Image.open(imagePath) as image:
        # RESIZING AND GRAYSCALE
        image =grayscaling(resizing(image))

        # ASCII CONVERTION
        newImage = asciiConvertion(image)

        with open('ASCII_Image.txt', 'w') as f:
            f.write(newImage)

main()