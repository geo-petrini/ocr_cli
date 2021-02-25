import argparse
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

"""
Lettura immaggine e scrittura del output nel file.

author: Viktorija Tilevska
version: 11.02.2012
last change: 25.02.2021
"""

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\vikto\\Documenti\\ocr_cli\\src\\Tesseract-OCR\\tesseract.exe'

# ------ Creazione parametri -----------
parser = argparse.ArgumentParser(usage="stats [-h] src dest lang name [-stats]")
parser.add_argument('source', type=str, help='source file path, could also be a directory')
parser.add_argument('-dest', default=".\scans_reader", type=str, help='output file path. Default directory: <.\scans>')
parser.add_argument('-lang', default="eng", type=str, choices=['eng', 'ita'], help='the language. Choose between it(italian) or en(english). Default is en')
parser.add_argument('-prefix', default=".\scan_1", type=str, help='output file name, if there are more files it defines the prefix')

args = parser.parse_args()

source = args.source
dest = args.dest
lang = args.lang
prefix = args.prefix

def read(img_to_str):
    txt = pytesseract.image_to_string(Image.open(img_to_str), lang=lang)
    print("read file")
    return txt

def write_to_txt(dest):
    #path = "{}/{}.txt".format(args.dest, args.prefix) #gestire il '/' !!
    '''
    if dest == ".\scans":
        dest = ".\scans\{}.txt".format(args.prefix)
    '''
    
    path = ".\scans_reader"

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    
    os. chdir(path)
    
    
    with open(prefix + ".txt",'a+') as outfile:
        outfile.write(read(source))    
    

    '''
    handle = open(dest + ".txt", "a+")
    print("open file")

    if handle.writable():
        handle.write(read(source))
        print("w file")
    
    handle.close()
    '''

write_to_txt(args.dest)