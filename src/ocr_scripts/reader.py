import argparse, pytesseract, logging, sys, os.path
from pathlib import Path
from os import path
try:
    from PIL import Image
except ImportError:
    import Image

"""
Lettura immaggine e scrittura del output nel file.

author: Viktorija Tilevska, Thaisa De Torre
version: 11.02.2012
last change: 01.04.2021
"""

# -----------------------------------------------------------------------
# Fa lo scan di tutti i file validi. Se non ci sono file validi il programma finisce
#
# args: dizionario di argomenti da controllare
# -----------------------------------------------------------------------
def scan(args):
    valid_files = validate_source(args.source)
    files_text = {}

    if len(valid_files) != 0:
        for f in valid_files:
            files_text[f] = {}
            files_text[f]['txt'] = get_text(f, args.lang)

            #with open(args.prefix, 'w+') as outfile:
            #    outfile.write(get_text(f, args.lang))
            #logging.info(f"Il file {args.prefix} e' stato creato")

        return files_text

    else:
        logging.error("Program stopped. No valid files were inserted.")
        sys.exit(1)
    

# -----------------------------------------------------------------------
# Fa tutti i controlli e i cambiamenti in modo da avere una lista con solamente
# i file validi da scannerizzare.
#
# source: lista con i percorsi sorgente
# return: una lista con tutti i percorsi validi per l'ocr
# -----------------------------------------------------------------------
def validate_source(source):
    # quando metti una cartella non riesce ad accedere i file, bisogna modificare il metodo check_permission()
    valid_files = [] #contiene tutti i file validi (jpg, png)
    file_list = len(source)
    logging.info(f"Number of files inserted: {file_list}")

    for img in source:
        logging.debug("for in  source")
        if os.access(img, os.R_OK):
            logging.debug("readable")
        else:
            logging.debug("not readable")
            
        if path.isfile(img):
            logging.debug("is file")

            if is_valid(img):
                valid_files.append(img)
        elif path.isdir(img):
            logging.debug("is dir")
            dir_list = get_dir_content(img)
            logging.debug(f"dir list: {dir_list}")

            for f in dir_list:
                if is_valid(f):
                    valid_files.append(img)

    # controllare se è una mask

    logging.debug(f"List of valid files ({len(valid_files)}): {valid_files}")
    return valid_files

# -----------------------------------------------------------------------
# Controlla se il formato del file al percorso path sia accettato dall'ocr (png o jpg o jpeg). 
#
# src: percorso del file da controllare
# return: true se il formato è accettato, altrimenti false
# -----------------------------------------------------------------------            
def is_valid(src):
    valid = False
    valid_extensions = ['.png', '.jpg', '.jpeg']
    file_ext = os.path.splitext(src)[-1]
    if file_ext in valid_extensions and check_permission(src):
        valid = True
        logging.debug(f"File {src} is valid")
    else:       
        logging.error("Error: A file has non been accepted. Please insert PNG and/or JPG/JPEG files")
        sys.exit(1)
    return valid

# --------------------------------------------------
# Controlla se il file è accessibile in lettura
#
# path: il percorso del file da controllare 
# returns: true se il file è accessibile, altrimenti ritorna false
# -------------------------------------------------
def check_permission(path):
    # migliorare questa parte
    valid = False
    try:
        with open(path) as f:
            valid = True
    except IOError:
        logging.warning(f"File {path} is not readable")

    return valid

# ------------------------------------------------------------
# Prende e ritorna il contenuto della cartella nel percorso path.
#
# path: percorso della cartella
# returns: una lista con i file contenuti nella cartella
# ------------------------------------------------------------
def get_dir_content(path):
    if len(os.listdir(path)) != 0:
        return os.listdir(path)
    else:
        logging.debug(f"The directory {path} is empty")
        return None

# -----------------------------------------------------------------------
# Legge il contenuto di una immagine 
#
# f: il percorso del file
# lang: la lingua
# return: una stringa con il contenuto dell'immagine
# ----------------------------------------------------------------------- 
def get_text(f, lang):
    try:
        text = pytesseract.image_to_string(Image.open(f), lang)
        return text
    except FileNotFoundError as fnf_error:
        logging.exception(f"Error: file {f} not found")
        return None

#https://docs.python.org/3/library/os.path.html link utile per lavorare con i percorsi
# ----------------------------------------------------------------------- 
# riceve l'output da scrivere
#
# funzionamento:
#    ricevo output da scrivere
#    controllo dest
#       esiste? 
#           posso scrivere? 
#    altrimenti creo dir/file
#    
#    controllo prefix
#       è valido per nome file?
#   --------------------------------
# descrizione metodo [...]
#
# output: è un dizionario contente l'associazione tra immagine e testo
#   scannerizzato insieme ad altre info.
# dest: la destinazione in cui scrivere l'output. Se è un file scrive tutto li,
#    se è una cartella salverà le scansioni in quella dir.
# prefix: il prefisso che avrà il file di output per evitare duplicati
#    nella stessa cartella.
# ----------------------------------------------------------------------- 
# def write_output(output, dest, prefix):
#     if dest.exists():
#         if dest.isWritable():
#             logging.debug("dest exists and is writable")
            
#             if path.isdir(dest):
#                 logging.debug("dest is dir")
#                 #check_prefix()
                
                
#             else:
#                 # sovrascrive il file ---> ??? richiedere consenso a user ???
#                 logging.debug("dest is file")
#                 with open(dest, 'w') as f:
#                     f.write(output)
#                 logging.warning("dest file overwrote")

# # -------------------------------
# # gestisce il prefisso del file di destinazione per non avere duplicati
# #
# # -------------------------------
# def check_prefix():
#     outName = prefix + ".txt"
#     if outName.exists():
#         outName = prefix + "_"+id+".txt"
        
#         fore file in dirContent:
#             ####################
#     else:
#         if isWritable:
#             create file dest/outName
