import argparse
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

"""

Lettura immaggine e scrittura del output nel file
author: Viktorija Tilevska
version: 11.02.2012

"""

# creare parametri necessari
parser = argparse.ArgumentParser(usage="stats [-h] src dest lang name [-stats]")
parser.add_argument('source', type=str, help='source file path, could also be a directory')

args = parser.parse_args()

source = args.source

print(pytesseract.image_to_string(Image.open(source)))
