import argparse, os, pytesseract, logging
try:
    from PIL import Image
except ImportError:
    import Image

"""
Lettura immaggine e scrittura del output nel file.

author: Viktorija Tilevska
version: 11.02.2012
last change: 04.03.2021
"""

# -----------------------------------------------------------------------
# Controlla se il formato dell'immagine passata dal utente è accettato.
#
# source: il percorso dell'immagine da leggere
# dest: il percorso dove verranno salvati i file
# lang: il linguaggio in qui leggere l'immagine
# prefix: il nome del file
# -----------------------------------------------------------------------
def check_img_type(source, dest, lang, prefix):
    image_ext = os.path.splitext(source)[-1]
    if image_ext.lower() == ".png" or image_ext.lower() == ".jpg":
        create_output_file(source, dest, lang, prefix)
    else:       
        logging.info("Error: Formato non accettato. Inserire immagini di tipo .png e/o .jpg")

def multi_image(source, dest, lang, prefix):
    if len(source) > 1:
        for path in source:
            check_img_type(path, dest, lang, prefix)


# --------------------------------------------------------------------------
# Crea la cartella passata dall'utente se essa non esiste.
# Dopo averla creata, o se esiste già, entra nella cartella di destinazione.
#
# dest: il percorso dove verranno salvati i file
# --------------------------------------------------------------------------
def create_and_change_directory(dest):
    try:
        os.mkdir(dest)
    except OSError:
        logging.info(f"La cartella {dest} esiste già")
    else:
        logging.info(f"La cartella {dest} è stata creata")

    os.chdir(dest)

# -----------------------------------------------------------
# Crea il file e scrive nell'esso il contenuto dell'immagine.
#
# file_name: il nome del file da creare
# text_to_write: il testo da inserire nel file 
# -----------------------------------------------------------
def write_file(file_name, text_to_write):
    with open(file_name, 'w+') as outfile:
        outfile.write(text_to_write)
        logging.info(f"Il file {file_name} è stato creato")

# -----------------------------------------------------------
# Se c'è un file con lo stesso nome dentro la cartella, crea il file aggiungendogli,
# alla fine, un numero in base al numero degli file con lo stesso nome.
# ex: scan.txt, scan_1.txt, scan_2.txt, ecc...
#
# file_name: il nome del file da creare
# text_to_write: il testo da inserire nel file 
# -----------------------------------------------------------
def write_existing_file(file_name, text_to_write):
    existing_file_name = os.path.splitext(file_name)
    name_id = existing_file_name[0]
    id = file_id[-1]
    
    # e se ci sono 2 file che si chiamano 492850.png?
    if id.isdigit():
        id = id + 1
    else:
        id = 1

    logging.debug(f"id: {id}")
    out_file_name = prefix + f"_{id}.txt"
    logging.debug(f"out name: {out_file_name}")

    write_file(out_file_name, text_to_write)


# ---------------------------------------------------------
# Crea il file di output nella cartella specificata dall'utente,
# nella ligua specificata dall'utente e con il nome specificato dall'utente.
# 
# source: il percorso dell'immagine da leggere
# dest: il percorso dove verranno salvati i file
# lang: il linguaggio in qui leggere l'immagine
# prefix: il nome del file
# ---------------------------------------------------------
def create_output_file(source, dest, lang, prefix): 
    create_and_change_directory(dest)
    logging.debug(f"src to open: {source}")
    logging.debug(f"img open src: {Image.open(source)}")
    text_to_write = pytesseract.image_to_string(Image.open(source), lang)
    file_name = f"{prefix}.txt"
    fileslist = os.listdir()
    
    if not fileslist:
        write_file(file_name, text_to_write)
        logging.debug(f"w file ok")
    else:
        if all(f in file_name for f in fileslist):
            write_existing_file(file_name, text_to_write)
        else:
            write_file(file_name, text_to_write)
