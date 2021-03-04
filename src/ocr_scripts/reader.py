import argparse
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import logging
import log_handler

"""
Lettura immaggine e scrittura del output nel file.

author: Viktorija Tilevska
version: 11.02.2012
last change: 25.02.2021
"""

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
        logging.info("La cartella %s esiste già" % dest)
    else:
        logging.info("La cartella %s è stata creata" % dest)

    os.chdir(dest)
    fileslist = os.listdir()
    file_name = f"{prefix}.txt"
    id = 0
    logging.debug(f"id: {id}")
    out_file_name = prefix + f"_{id+1}.txt"
    logging.debug(f"out name: {out_file_name}")
    
    
    if not fileslist:
        with open(file_name, 'w+') as outfile:
            outfile.write(text_to_write)
            logging.info(f"Il file {file_name} è stato creato") 
    else:  
        if all(f in file_name for f in fileslist):
            with open(out_file_name, 'w+') as outfile:
                outfile.write(text_to_write)
                logging.info(f"Il file {file_name} è stato creato")
        else:
            with open(file_name, 'w+') as outfile:
                outfile.write(text_to_write)
                logging.info(f"Il file {file_name} è stato creato")
        
