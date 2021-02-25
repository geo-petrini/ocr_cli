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
parser.add_argument('-prefix', default=".\scan", type=str, help='output file name, if there are more files it defines the prefix')

args = parser.parse_args()

# ---------------------------------------------------------
# Legge una o più immagini e ne crive il contenuto nei file .txt.
# 
# source: il percorso della immagine da leggere
# dest: il percorso dove vengono slvati i file
# lang: il linguaggio in qui leggere l'immagine
# prefix: il nome del file
# ---------------------------------------------------------
def write_to_txt(source, dest, lang, prefix):
    text_to_write = pytesseract.image_to_string(Image.open(source), lang=lang)

    try:
        os.mkdir(dest)
    except OSError:
        print ("The directory %s already exists" % dest)
    else:
        print ("Successfully created the directory %s " % dest)

    os.chdir(dest)
    fileslist = os.listdir()
    file_name = f"{prefix}.txt"
    id = 1
    out_file_name = prefix + f"({id}).txt"
    print(fileslist)
    
    if not fileslist:
        with open(file_name, 'w+') as outfile:
            outfile.write(text_to_write)

    
    for f in fileslist:
        if f == file_name:
            with open(out_file_name, 'w+') as outfile:
                outfile.write(text_to_write)
                id += 1
                print(id)
        else:
            with open(file_name, 'w+') as outfile:
                outfile.write(text_to_write)
          
write_to_txt(args.source, args.dest, args.lang, args.prefix)